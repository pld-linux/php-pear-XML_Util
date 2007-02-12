%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Util
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - XML utility class
Summary(pl.UTF-8):   %{_pearname} - klasa narzędziowa do obróbki XML-a
Name:		php-pear-%{_pearname}
Version:	1.1.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5b28a79000d47f2bde73c10ca191e402
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
