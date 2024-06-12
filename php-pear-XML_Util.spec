#
# Conditional build:
%bcond_with	bootstrap	# bootstrap build without PEAR installed (for first php-pear-PEAR installation)

%define		status		stable
%define		pearname	XML_Util
Summary:	%{pearname} - XML utility class
Summary(pl.UTF-8):	%{pearname} - klasa narzędziowa do obróbki XML-a
Name:		php-pear-%{pearname}
Version:	1.4.5
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	3e048e6b5822d0d2f7f4d9129fcd5df8
URL:		http://pear.php.net/package/XML_Util/
%if %{without bootstrap}
BuildRequires:	php-pear-PEAR
%endif
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php(pcre)
Requires:	php-pear
Requires:	php-pear-PEAR-core
Obsoletes:	php-pear-XML_Util-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Selection of methods that are often needed when working with XML
documents. Functionality includes creating of attribute lists from
arrays, creation of tags, validation of XML names and more.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Zbiór metod często stosowanych podczas pracy z dokumentami XML.
Możliwość między innymi tworzenia listy atrybutów z tablic, tworzenia
znaczników, sprawdzania poprawności nazw XML oraz wiele innych.

Ta klasa ma w PEAR status: %{status}.

%prep
%if %{without bootstrap}
%pear_package_setup
%else
%setup -q -c -n %{pearname}-%{version}
%{__mv} %{pearname}-%{version}/* .
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}

%if %{without bootstrap}
%pear_package_install
%else
cp -pr XML $RPM_BUILD_ROOT%{php_pear_dir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%if %{without bootstrap}
%doc install.log docs/%{pearname}/examples
%{php_pear_dir}/.registry/xml_util.reg
%endif
%{php_pear_dir}/XML/Util.php
