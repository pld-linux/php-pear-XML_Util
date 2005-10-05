%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Util
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - XML utility class
Summary(pl):	%{_pearname} - klasa narzêdziowa do obróbki XML-a
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	528278996240d47a07e4273fb7bde841
URL:		http://pear.php.net/package/XML_Util/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.2.0
Requires:	php-pcre
Requires:	php-pear
Requires:	php-pear-PEAR
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Selection of methods that are often needed when working with XML
documents. Functionality includes creating of attribute lists from
arrays, creation of tags, validation of XML names and more.

In PEAR status of this package is: %{_status}.

%description -l pl
Zbiór metod czêsto stosowanych podczas pracy z dokumentami XML.
Mo¿liwo¶æ miêdzy innymi tworzenia listy atrybutów z tablic, tworzenia
tagów, sprawdzania poprawno¶ci nazw XML oraz wiele innych.

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
