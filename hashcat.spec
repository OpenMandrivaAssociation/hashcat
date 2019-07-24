Name:           hashcat
Version:	5.1.0
Release:	1
Summary:        CPU-based password recovery utility
License:        MIT
Group:          Productivity/Security
Url:            https://hashcat.net/
Source0:        https://github.com/hashcat/hashcat/archive/v%version.tar.gz
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig(OpenCL)
ExclusiveArch:  %ix86 x86_64 znver1

%description
Hashcat is an advanced CPU-based password recovery utility,
supporting seven unique modes of testing for over 100 optimized
hashing algorithms.

%prep
%setup -q

%build
sed -i "s/-O2//" src/Makefile
sed -i "/LFLAGS                  += -s/d" src/Makefile

%make CC=%{__cc} COMPTIME=0 our_CFLAGS="%optflags" PREFIX="%_prefix"

%install
%make_install PREFIX="%_prefix" DOCUMENT_FOLDER="%_docdir/%name"

%check
# ./hashcat --force -a 3 -m 1500 nQCk49SiErOgk

%files
%_bindir/hashcat
%_datadir/%name/
%_docdir/%name/
