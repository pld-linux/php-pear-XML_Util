%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       Util
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - XML Utility class
Summary(pl):	%{_pearname} - klasa narzêdziowa do obróbki XML-a
Name:		php-pear-%{_pearname}
Version:	0.5.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e76993585c2d3d755ea7cf53261a014a
URL:		http://pear.php.net/package/XML_Util/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Selection of methods that are often needed when working with XML
documents. Functionality includes creating of attribute lists from
arrays, creation of tags, validation of XML names and more.

This class has in PEAR status: %{_status}.

%description -l pl
Zbiór metod czêsto stosowanych podczas pracy z dokumentami XML.
Mo¿liwo¶æ miêdzy innymi tworzenia listy atrybutów z tablic, tworzenia
tagów, sprawdzania poprawno¶ci nazw XML oraz wiele innych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
