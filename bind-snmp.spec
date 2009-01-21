# TODO
# - register cacti template (see template-cacti-plugin.spec)?
%include	/usr/lib/rpm/macros.perl
Summary:	Bind SNMP script
Summary(pl.UTF-8):	Skrypt Bind SNMP
Name:		bind-snmp
Version:	1.7
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.bayour.com/bind9-snmp/bind9-snmp_%{version}.tgz
# Source0-md5:	e04c7116a100a619cf81f9b9fb8943e1
URL:		http://www.bayour.com/bind9-snmp/
BuildRequires:	rpm-perlprov
Requires:	bind >= 9.0.0
Requires:	perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webadminroot /usr/share/cacti

%description
This is a pass-through script for SNMP that gives all the Bind9
statistics that can be (is) retrieved with 'rndc status'.

%description -l pl.UTF-8
To jest skrypt dla SNMP dostarczający wszystkie statystyki Binda 9,
jakie można pobrać za pomocą polecenia 'rndc status'.

%package -n net-snmp-mibs-bind
Summary:	MIBs for BIND9
Summary(pl.UTF-8):	MIB-y dla BIND-a 9
Group:		Applications/System
Requires:	net-snmp-mibs

%description -n net-snmp-mibs-bind
MIBs for BIND9.

%description -n net-snmp-mibs-bind -l pl.UTF-8
MIB-y dla BIND-a 9.

%package -n cacti-bind
Summary:	BIND9 plugin for Cacti
Summary(pl.UTF-8):	Wtyczka BIND9 dla Cacti
Group:		Applications/System
Requires:	net-snmp-mibs-bind = %{version}-%{release}
Requires:	cacti

%description -n cacti-bind
BIND9 plugin for Cacti.

%description -n cacti-bind -l pl.UTF-8
Wtyczka BIND9 dla Cacti.

%prep
%setup -q -n bind9-snmp-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webadminroot}/resource/snmp_queries
install -d $RPM_BUILD_ROOT%{_datadir}/snmp/mibs
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{snmp,cron.d}
install -d $RPM_BUILD_ROOT%{perl_vendorlib}

install {*.pl,*.stub} $RPM_BUILD_ROOT%{_sysconfdir}/snmp
install *.xml $RPM_BUILD_ROOT%{webadminroot}/resource/snmp_queries
install BAYOUR-COM-MIB.txt $RPM_BUILD_ROOT%{_datadir}/snmp/mibs
install *.pm $RPM_BUILD_ROOT%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt UPGRADE.txt
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/snmp/bind9-snmp-stats.pl
%{_sysconfdir}/snmp/snmp*.conf.stub
%{perl_vendorlib}/BayourCOM_SNMP.pm

%files -n net-snmp-mibs-bind
%defattr(644,root,root,755)
%{_datadir}/snmp/mibs/BAYOUR-COM-MIB.txt

%files -n cacti-bind
%defattr(644,root,root,755)
%{webadminroot}/resource/snmp_queries/cacti_host_template_bind9_snmp_machine.xml
%{webadminroot}/resource/snmp_queries/bind9-stats_domains.xml
%{webadminroot}/resource/snmp_queries/bind9-stats_totals.xml
