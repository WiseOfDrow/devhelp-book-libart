Summary:	DevHelp book: libart
Summary(pl.UTF-8):	Książka do DevHelpa o libart
Name:		devhelp-book-libart
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/libart.tar.gz
# Source0-md5:	bbeaa253f578cc07f5cfb598942de354
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about libart.

%description -l pl.UTF-8
Książka do DevHelpa o libart.

%prep
%setup -q -c -n libart

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/libart,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/libart.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/libart

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
