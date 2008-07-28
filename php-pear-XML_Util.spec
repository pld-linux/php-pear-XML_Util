%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Util
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - XML utility class
Summary(pl.UTF-8):	%{_pearname} - klasa narzędziowa do obróbki XML-a
Name:		php-pear-%{_pearname}
Version:	1.2.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f680736898dd77f5f254347aca0789c0
URL:		http://pear.php.net/package/XML_Util/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(pcre)
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Selection of methods that are often needed when working with XML
documents. Functionality includes creating of attribute lists from
arrays, creation of tags, validation of XML names and more.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Zbiór metod często stosowanych podczas pracy z dokumentami XML.
Możliwość między innymi tworzenia listy atrybutów z tablic, tworzenia
tagów, sprawdzania poprawności nazw XML oraz wiele innych.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/%{_pearname}
