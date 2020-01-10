Name: hunspell-es
Summary: Spanish hunspell dictionaries
Version: 0.6
Release: 4%{?dist}
Epoch: 1
Source: http://forja.rediris.es/frs/download.php/2618/es_ANY.oxt
Group: Applications/Text
URL: https://forja.rediris.es/projects/rla-es/
License: LGPLv3+ or GPLv3+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Spanish (Spain, Mexico, etc.) hunspell dictionaries.

%prep
%setup -q -c -n hunspell-es

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p es_ANY.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/es.dic
cp -p es_ANY.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/es.aff

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
es_ES_aliases="es_ES es_AR es_BO es_CL es_CO es_CR es_CU es_DO es_EC es_GT es_HN es_MX es_NI es_PA es_PE es_PR es_PY es_SV es_US es_UY es_VE"

for lang in $es_ES_aliases; do
	ln -s es.aff $lang.aff
	ln -s es.dic $lang.dic
done
popd

%files
%doc README.txt Changelog.txt GPLv3.txt MPL-1.1.txt LGPLv3.txt
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:0.6-4
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Ismael Olea <ismael@olea.org> - 1:0.6-1
- update to 0.6

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081215-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081215-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081215-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081215-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081215-1
- latest version

* Mon Sep 29 2008 Caolan McNamara <caolanm@redhat.com> - 0.20051031-3
- add es_CU as Cuba for OOo

* Tue Jul 08 2008 Caolan McNamara <caolanm@redhat.com> - 0.20051031-2
- add es_US

* Mon Aug 20 2007 Caolan McNamara <caolanm@redhat.com> - 0.20051031-1
- latest version
- clarify license version

* Thu Aug 09 2007 Caolan McNamara <caolanm@redhat.com> - 0.20050510-2
- clarify license version

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20050510-1
- initial version
