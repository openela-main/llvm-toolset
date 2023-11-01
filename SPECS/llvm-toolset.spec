%global maj_ver 14
%global min_ver 0
%global patch_ver 6
#global rc_ver 0
%global baserelease 1

Summary: Package that installs llvm-toolset
Name: llvm-toolset
Version: %{maj_ver}.%{min_ver}.%{patch_ver}
Release: %{baserelease}%{?rc_ver:.rc%{rc_ver}}%{?dist}
License: NCSA

Requires: clang = %{version}

Requires: llvm = %{version}
%ifnarch s390x
Requires: lld = %{version}
%endif

%description
This is the main package for llvm-toolset.

%files

%changelog
* Wed Jul 20 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.6-1
- Update to 14.0.6

* Wed Jun 22 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.5-1
- Update to 14.0.5

* Wed Apr 13 2022 Timm Bäder <tbaeder@redhat.com> - 14.0.0-1
- Update to 14.0.0

* Fri Feb 04 2022 Tom Stellard <tstellar@redhat.com> - 13.0.1-1
- 13.0.1 Release

* Wed Oct 13 2021 Timm Bäder <tbaeder@redhat.com> - 13.0.0-1
- Release 13.0.0
- Remove lld dependency. rhbz#2011107

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 12.0.1-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jul 14 2021 Tom Stellard <tstellar@redhat.com> - 12.0.1-1
- 12.0.1 Release

* Tue May 04 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0-2
- Fix release string

* Mon May 3 2021 Tom Stellard <tstellar@redhat.com> - 12.0.0-1
- 12.0.0 Release

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 11.1.0-0.2.rc2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Mon Feb 15 2021 Serge Guelton - 11.1.0-0.1.rc2
- 11.1.0 release

* Tue Jan 12 2021 sguelton@redhat.com - 11.0.1-1
- 11.0.1 release

* Wed Nov 11 2020 sguelton@redhat.com - 11.0.0-1
- 11.0.0 release

* Wed Sep 23 2020 sguelton@redhat.com - 11.0.0-0.2.rc2
- Fix version number

* Mon Sep 21 2020 sguelton@redhat.com - 11.0.0-0.1.rc2
- 11.0.1.rc2 Release

* Fri Jul 24 2020 sguelton@redhat.com - 10.0.1-1
- 10.0.1 Release

* Tue Apr 14 2020 sguelton@redhat.com - 10.0.0-1
- 10.0.0 Release

* Mon Jan 06 2020 Tom Stellard <tstellar@redhat.com> - 9.0.1-1
- Fix version number

* Mon Jan 06 2020 Tom Stellard <tstellar@redhat.com> - 9.0.1-1
- 9.0.1 Release

* Tue Oct 01 2019 Tom Stellard <tstellar@redhat.com> - 9.0.0-2
- 9.0.0 Release

* Thu Aug 1 2019 sguelton@redhat.com - 8.0.1-1
- 8.0.1 release

* Thu Jun 13 2019 sguelton@redhat.com - 8.0.1-0.1.rc2
- 8.0.1rc2 Release

* Wed Apr 17 2019 sguelton@redhat.com - 8.0.0-1
- 8.0.0 Release

* Sat Dec 15 2018 Tom Stellard <tstellar@redhat.com> - 7.0.1-1
- 7.0.1 Release

* Mon Dec 10 2018 Tom Stellard <tstellar@redhat.com> - 7.0.1-0.1.rc3
- 7.0.1-rc3 Release

* Thu Oct 11 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-5
- Add empty files section

* Mon Oct 01 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-4
- Drop SCL macros

* Fri Sep 21 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-3
- Install lld by default

* Fri Aug 03 2018 Vít Ondruch <vondruch@redhat.com> - 6.0.1-2
- scl_files hack is not needed anymore.

* Tue Jul 10 2018 Tom Stellard <tstellar@redhat.com> - 6.0.1-1
- LLVM 6.0.1 release

* Fri Feb 16 2018 Tilmann Scheller <tschelle@redhat.com> - 5.0.1-5
- Move %enable_llvmtoolset7 macro to the -build subpackage to avoid conflicts
  between multiple definitions of %scl when using llvm-toolset-7 to build a SCL

* Thu Feb 08 2018 Tilmann Scheller <tschelle@redhat.com> - 5.0.1-4
- Add %enable_llvmtoolset7 macro to make it easier to activate llvm-toolset-7
  during package builds.

* Fri Feb 02 2018 Tom Stellard <tstellar@redhat.com> - 5.0.1-3
- Only install build tools

* Fri Feb 02 2018 Tom Stellard <tstellar@redhat.com> - 5.0.1-2
- Work around bug in scl_files

* Wed Jan 17 2018 Tom Stellard <tstellar@redhat.com> - 5.0.1-1
- LLVM 5.0.1 release

* Wed Jan 17 2018 Tom Stellard <tstellar@redhat.com> - 4.0.1-5
- Drop dockerfiles package

* Wed Oct 04 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-4
- Update Dockerfile

* Wed Sep 20 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-3
- Update Dockerfile

* Wed Aug 09 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-2
- Add docker file

* Wed Jun 21 2017 Tom Stellard <tstellar@redhat.com> - 4.0.1-1
- 4.0.1 Release.

* Wed Jun 21 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-6
- Fix Requires for lldb, this package is not built on all arches

* Mon Jun 05 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-5
- Remove scldevel package

* Mon Jun 05 2017 Tom Stellard <tstellar@rehat.com> - 4.0.0-4
- Remove unnecessary code

* Fri May 12 2017 Tom Stellard <tstellar@redhat.com> - 4.0.0-3
- Add clang, lldb, and python-lit to Requires

* Wed May 10 2017 Tilmann Scheller <tschelle@redhat.com> - 4.0.0-2
- Update PYTHONPATH to point to the scl's Python site-packages directory

* Mon Apr 24 2017 Tom Stellard <tstellar@redhat.com> 4.0.0-1
- Initial package
