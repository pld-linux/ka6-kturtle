#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.12.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kturtle
Summary:	kturtle
Summary(pl.UTF-8):	kturtle
Name:		ka6-%{kaname}
Version:	25.12.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a298e28a7e89110709ecb47ea51b83bc
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-knewstuff-devel >= %{kframever}
BuildRequires:	kf6-ktextwidgets-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTurtle is an educational programming environment that aims to make
learning how to program as easily as possible. To achieve this KTurtle
makes all programming tools available from the user interface. The
programming language used is TurtleScript which allows its commands to
be translated.

%description -l pl.UTF-8
KTurtle to edukacyjne środowisko programistyczne, którego celem jest
nauczanie programowania tak łatwo, jak to tylko możliwe. Aby to
osiągnąć KTurtle udostępnia wszystkie narzędzia programistyczne z
interfejsu użytkownika. Używanym językiem programowania jest
TurtleScript, który pozwala by jego komendy były przetłumaczone.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kturtle
%{_desktopdir}/org.kde.kturtle.desktop
%{_iconsdir}/hicolor/*x*/apps/kturtle.png
%{_datadir}/metainfo/org.kde.kturtle.appdata.xml
%{_datadir}/knsrcfiles/kturtle.knsrc
