Summary:	Issue tracker for distributed SCMs
Name:		ditz
Version:	0.1
Release:	1
License:	Ruby
Source0:	http://rubyforge.org/frs/download.php/34859/ditz-0.1.tgz
# Source0-md5:	1ea135ab10fff82ed240d1cd5fc94f12
Group:		Development/Tools
Patch0:		%{name}-nogems.patch
Patch1:		%{name}-paths.patch
URL:	http://ditz.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-trollop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ditz is a simple, light-weight distributed issue tracker designed to work
with distributed version control systems like darcs and git. Ditz maintains
an issue database file on disk, written in a line-based and human-editable
format. This file is kept under version control, alongside project code.
Changes in issue state is handled by version control like code change:
included as part of a commit, merged with changes from other developers,
conflict-resolved in the standard manner, etc.

Ditz provides a simple, console-based interface for creating and updating
the issue database file, and some rudimentary HTML generation capabilities
for producing world-readable status pages. It offers no central public
method of bug submission.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
install %{_datadir}/setup.rb .

%build
mkdir lib/ditz
mv lib/*.rb lib/ditz/
mv lib/ditz/ditz.rb lib/
ruby setup.rb config --rbdir=%{ruby_rubylibdir} --sodir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/ditz
