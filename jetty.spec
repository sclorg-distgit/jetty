%global pkg_name jetty
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global addver v20130506

Name:           %{?scl_prefix}%{pkg_name}
Version:        9.0.3
Release:        8.9%{?dist}
Summary:        Java Webserver and Servlet Container

# Jetty is dual licensed under both ASL 2.0 and EPL 1.0, see NOTICE.txt
License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.project.git/snapshot/jetty-%{version}.%{addver}.tar.gz
Source1:        djetty.script
Source3:        jetty.logrotate
Source5:        %{pkg_name}.service
# MIT license text taken from Utf8Appendable.java
Source6:        LICENSE-MIT
Patch0:         %{pkg_name}-create-work-dir.patch
Patch4:         0004-Modify-dependencies.patch

BuildRequires:  %{?scl_prefix}geronimo-annotation
BuildRequires:  %{?scl_prefix}geronimo-jaspic-spec
BuildRequires:  %{?scl_prefix}geronimo-jta
BuildRequires:  %{?scl_prefix}geronimo-parent-poms
BuildRequires:  %{?scl_prefix}glassfish-el
BuildRequires:  %{?scl_prefix}glassfish-el-api
BuildRequires:  %{?scl_prefix}glassfish-jsp
BuildRequires:  %{?scl_prefix}glassfish-jsp-api
BuildRequires:  %{?scl_prefix}jakarta-taglibs-standard
BuildRequires:  %{?scl_prefix}javapackages-tools
BuildRequires:  %{?scl_prefix}javapackages-tools >= 0.7.0
BuildRequires:  %{?scl_prefix}jvnet-parent
BuildRequires:  %{?scl_prefix}ant
BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}maven-dependency-plugin
BuildRequires:  %{?scl_prefix}maven-enforcer-plugin
BuildRequires:  %{?scl_prefix}maven-shade-plugin
BuildRequires:  %{?scl_prefix}maven-war-plugin
BuildRequires:  %{?scl_prefix}objectweb-asm
BuildRequires:  %{?scl_prefix}slf4j-api
BuildRequires:  %{?scl_prefix}tomcat-lib
BuildRequires:  %{?scl_prefix}geronimo-parent-poms
BuildRequires:  %{?scl_prefix}maven-plugin-build-helper

BuildRequires:  %{?scl_prefix}javamail
BuildRequires:  %{?scl_prefix}jetty-parent
BuildRequires:  %{?scl_prefix}jetty-distribution-remote-resources
BuildRequires:  %{?scl_prefix}jetty-build-support
BuildRequires:  %{?scl_prefix}jetty-version-maven-plugin
BuildRequires:  %{?scl_prefix}jetty-toolchain
BuildRequires:  %{?scl_prefix}jetty-assembly-descriptors
BuildRequires:  %{?scl_prefix}jetty-test-policy
BuildRequires:  %{?scl_prefix}jetty-artifact-remote-resources

BuildArch:      noarch

Requires:       %{name}-client               = %{version}-%{release}
Requires:       %{name}-annotations          = %{version}-%{release}
Requires:       %{name}-client               = %{version}-%{release}
Requires:       %{name}-continuation         = %{version}-%{release}
Requires:       %{name}-deploy               = %{version}-%{release}
Requires:       %{name}-http                 = %{version}-%{release}
Requires:       %{name}-io                   = %{version}-%{release}
Requires:       %{name}-jaas                 = %{version}-%{release}
Requires:       %{name}-jmx                  = %{version}-%{release}
Requires:       %{name}-jndi                 = %{version}-%{release}
Requires:       %{name}-plus                 = %{version}-%{release}
Requires:       %{name}-proxy                = %{version}-%{release}
Requires:       %{name}-rewrite              = %{version}-%{release}
Requires:       %{name}-security             = %{version}-%{release}
Requires:       %{name}-server               = %{version}-%{release}
Requires:       %{name}-servlet              = %{version}-%{release}
Requires:       %{name}-servlets             = %{version}-%{release}
Requires:       %{name}-util                 = %{version}-%{release}
Requires:       %{name}-webapp               = %{version}-%{release}
Requires:       %{name}-websocket-api        = %{version}-%{release}
Requires:       %{name}-websocket-common     = %{version}-%{release}
Requires:       %{name}-websocket-server     = %{version}-%{release}
Requires:       %{name}-websocket-servlet    = %{version}-%{release}


%description
%global desc \
Jetty is a 100% Java HTTP Server and Servlet Container. This means that you\
do not need to configure and run a separate web server (like Apache) in order\
to use Java, servlets and JSPs to generate dynamic content. Jetty is a fully\
featured web server for static and dynamic content. Unlike separate\
server/container solutions, this means that your web server and web\
application run in the same process, without interconnection overheads\
and complications. Furthermore, as a pure java component, Jetty can be simply\
included in your application for demonstration, distribution or deployment.\
Jetty is available on all Java supported platforms.
%{desc}
%global extdesc %{desc}\
\
This package contains

%package        project
Summary:        POM files for Jetty

%description    project
%{extdesc} %{summary}.

%package        annotations
Summary:        annotations module for Jetty

%description    annotations
%{extdesc} %{summary}.

%package        ant
Summary:        ant module for Jetty

%description    ant
%{extdesc} %{summary}.

%package        client
Summary:        client module for Jetty

%description    client
%{extdesc} %{summary}.

%package        continuation
Summary:        continuation module for Jetty

%description    continuation
%{extdesc} %{summary}.

%package        deploy
Summary:        deploy module for Jetty

%description    deploy
%{extdesc} %{summary}.

%package        http
Summary:        http module for Jetty

%description    http
%{extdesc} %{summary}.

%package        io
Summary:        io module for Jetty

%description    io
%{extdesc} %{summary}.

%package        jaas
Summary:        jaas module for Jetty

%description    jaas
%{extdesc} %{summary}.

%package        jaspi
Summary:        jaspi module for Jetty

%description    jaspi
%{extdesc} %{summary}.

%package        jmx
Summary:        jmx module for Jetty

%description    jmx
%{extdesc} %{summary}.

%package        jndi
Summary:        jndi module for Jetty

%description    jndi
%{extdesc} %{summary}.

%package        jsp
Summary:        jsp module for Jetty

%description    jsp
%{extdesc} %{summary}.

%package        jspc-maven-plugin
Summary:        jspc-maven-plugin module for Jetty

%description    jspc-maven-plugin
%{extdesc} %{summary}.

%package        maven-plugin
Summary:        maven-plugin module for Jetty

%description    maven-plugin
%{extdesc} %{summary}.

%package        monitor
Summary:        monitor module for Jetty

%description    monitor
%{extdesc} %{summary}.

%package        plus
Summary:        plus module for Jetty

%description    plus
%{extdesc} %{summary}.

%package        proxy
Summary:        proxy module for Jetty

%description    proxy
%{extdesc} %{summary}.

%package        rewrite
Summary:        rewrite module for Jetty

%description    rewrite
%{extdesc} %{summary}.

%package        runner
Summary:        runner module for Jetty

%description    runner
%{extdesc} %{summary}.

%package        security
Summary:        security module for Jetty

%description    security
%{extdesc} %{summary}.

%package        server
Summary:        server module for Jetty

%description    server
%{extdesc} %{summary}.

%package        servlet
Summary:        servlet module for Jetty

%description    servlet
%{extdesc} %{summary}.

%package        servlets
Summary:        servlets module for Jetty

%description    servlets
%{extdesc} %{summary}.

%package        start
Summary:        start module for Jetty

%description    start
%{extdesc} %{summary}.

%package        util
Summary:        util module for Jetty
# Utf8Appendable.java is additionally under MIT license
License:        (ASL 2.0 or EPL) and MIT

%description    util
%{extdesc} %{summary}.

%package        util-ajax
Summary:        util-ajax module for Jetty

%description    util-ajax
%{extdesc} %{summary}.

%package        webapp
Summary:        webapp module for Jetty

%description    webapp
%{extdesc} %{summary}.

%package        xml
Summary:        xml module for Jetty

%description    xml
%{extdesc} %{summary}.

%package        websocket-api
Summary:        websocket-api module for Jetty

%description    websocket-api
%{extdesc} %{summary}.

%package        websocket-client
Summary:        websocket-client module for Jetty

%description    websocket-client
%{extdesc} %{summary}.

%package        websocket-common
Summary:        websocket-common module for Jetty

%description    websocket-common
%{extdesc} %{summary}.

%package        websocket-parent
Summary:        POM file for jetty-websocket

%description    websocket-parent
%{extdesc} %{summary}.

%package        websocket-server
Summary:        websocket-server module for Jetty

%description    websocket-server
%{extdesc} %{summary}.

%package        websocket-servlet
Summary:        websocket-servlet module for Jetty

%description    websocket-servlet
%{extdesc} %{summary}.

%package        javadoc
Summary:        Javadoc for %{pkg_name}
# some MIT-licensed code (from Utf8Appendable) is used to generate javadoc
License:        (ASL 2.0 or EPL) and MIT

%description    javadoc
%{summary}.

%prep
%setup -q -n %{pkg_name}-%{version}.%{addver}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
for f in $(find . -name "*.?ar"); do rm $f; done
find . -name "*.class" -exec rm {} \;

%patch0 -p1 -b .sav
%patch4 -p1 -b .sav

# Use proper groupId for apache ant
%pom_xpath_replace "pom:groupId[text()='ant']" "<groupId>org.apache.ant</groupId>" jetty-ant/pom.xml

# Disable test and example artifacts
# they need more dependencies then we have time for right now :-)
# and also xmvn currently doesn't support .war
%pom_disable_module tests
%pom_disable_module examples

# Since tests are disabled, we don't have some jars
%pom_remove_dep :test-jetty-webapp jetty-distribution/pom.xml
%pom_remove_dep :test-proxy-webapp jetty-distribution/pom.xml
%pom_remove_dep :example-async-rest-webapp jetty-distribution/pom.xml
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='test-jetty-webapp']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='test-proxy-webapp']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='example-async-rest-webapp']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='test-jaas-webapp']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='test-jndi-webapp']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:artifactItem[pom:artifactId[text()='test-spec-webapp']]" jetty-distribution/pom.xml

# Missing jars (jetty-setuid-java-1.0.0.jar,jetty-setuid-java-1.0.0-config.jar)
%pom_xpath_remove "pom:execution[pom:id[text()='unpack-setuid-config']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:execution[pom:id[text()='copy-setuid-deps']]" jetty-distribution/pom.xml
# test-jaas-webapp artifact is disabled
%pom_xpath_remove "pom:execution[pom:id[text()='unpack-test-jaas-config']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:execution[pom:id[text()='unpack-test-jndi-config']]" jetty-distribution/pom.xml
%pom_xpath_remove "pom:execution[pom:id[text()='unpack-test-spec-config']]" jetty-distribution/pom.xml

# We don't have this plugin yet
%pom_remove_plugin :findbugs-maven-plugin jetty-websocket/pom.xml

# enforcer plugin constantly complains
%pom_remove_plugin :maven-enforcer-plugin

# Change servelt groupId to javax.servlet
%pom_xpath_inject "pom:project/pom:properties" "
    <servlet.spec.groupId>javax.servlet</servlet.spec.groupId>
    <servlet.spec.artifactId>servlet-api</servlet.spec.artifactId>
    <servlet.spec.version>3.0.20100224</servlet.spec.version>"

# Prevents problem with "Reporting mojo's can only be called from
# ReportDocumentRender". Investigate proper fix some other time?
%pom_remove_plugin :maven-pmd-plugin

# License plugin may be useful for upstream, but it has no use in
# Fedora.
%pom_remove_plugin :maven-license-plugin

# Remove unpack-config-deps from distribution
#
# This is needed because original code used classifiers to select subset
# of artifacts. Unfortunately there seems to be a weird bug affecting even
# upstream maven when this goes outside of reactor resolver. Or perhaps
# this is a weird feature.
#
# Our resolver obviously can't handle this so we have to unpack these
# manually before building distribution
%pom_xpath_remove "pom:execution[pom:id[text()='unpack-config-deps']]" jetty-distribution

# Disable SPDY for now as there are missing dependencies. SPDY needs
# Next Protocol Negotiation TLS Extension (NPN) for OpenJDK 7 or
# greater. We don't have this extension in Fedora.
# See: http://wiki.eclipse.org/Jetty/Feature/NPN
%pom_disable_module jetty-spdy
%pom_remove_dep org.eclipse.jetty.spdy: jetty-distribution

# Disable OSGi
%pom_disable_module jetty-osgi

# Disable NoSQL
%pom_disable_module jetty-nosql

# Disable Spring
%pom_disable_module jetty-spring

%pom_remove_dep :org.eclipse.jdt.core jetty-jsp

cp %{SOURCE1} djetty
cp %{SOURCE6} .

# Looks like all CDDL licensed content in tarball has been replaced,
# we don't need to install this license
rm LICENSE-CONTRIBUTOR/CDDLv1.0.txt
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
sed -i -e "s|/usr/share|%{_datadir}|g" djetty

%mvn_package :jetty-distribution __noinstall
# Separate package for main POM file
%mvn_package :jetty-project project

# we don't have all necessary dependencies to run tests
# missing test dep: org.eclipse.jetty.toolchain:jetty-test-helper
%mvn_build -f -s

cd jetty-distribution
rm -rf target/distribution
mkdir -p target/distribution
find .. -ipath '*target/*config.jar' | ( while read; do
  unzip $REPLY -x 'META-INF/*' -d target/distribution
done)
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files project -f .mfiles-project
%doc NOTICE.txt README.txt VERSION.txt LICENSE-eplv10-aslv20.html LICENSE-CONTRIBUTOR

%files util -f .mfiles-jetty-util
%doc NOTICE.txt README.txt VERSION.txt LICENSE-eplv10-aslv20.html LICENSE-CONTRIBUTOR
%doc LICENSE-MIT
%dir %{_javadir}/%{pkg_name}

%files annotations -f .mfiles-jetty-annotations
%files ant -f .mfiles-jetty-ant
%files client -f .mfiles-jetty-client
%files continuation -f .mfiles-jetty-continuation
%files deploy -f .mfiles-jetty-deploy
%files http -f .mfiles-jetty-http
%files io -f .mfiles-jetty-io
%files jaas -f .mfiles-jetty-jaas
%files jaspi -f .mfiles-jetty-jaspi
%files jmx -f .mfiles-jetty-jmx
%files jndi -f .mfiles-jetty-jndi
%files jsp -f .mfiles-jetty-jsp
%files jspc-maven-plugin -f .mfiles-jetty-jspc-maven-plugin
%files maven-plugin -f .mfiles-jetty-maven-plugin
%files monitor -f .mfiles-jetty-monitor
%files plus -f .mfiles-jetty-plus
%files proxy -f .mfiles-jetty-proxy
%files rewrite -f .mfiles-jetty-rewrite
%files runner -f .mfiles-jetty-runner
%files security -f .mfiles-jetty-security
%files server -f .mfiles-jetty-server
%files servlet -f .mfiles-jetty-servlet
%files servlets -f .mfiles-jetty-servlets
%files start -f .mfiles-jetty-start
%files util-ajax -f .mfiles-jetty-util-ajax
%files webapp -f .mfiles-jetty-webapp
%files xml -f .mfiles-jetty-xml
%files websocket-api -f .mfiles-websocket-api
%files websocket-client -f .mfiles-websocket-client
%files websocket-common -f .mfiles-websocket-common
%files websocket-parent -f .mfiles-websocket-parent
%files websocket-server -f .mfiles-websocket-server
%files websocket-servlet -f .mfiles-websocket-servlet

%files javadoc -f .mfiles-javadoc
%doc NOTICE.txt LICENSE*

%changelog
* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.3-8.9
- Mass rebuild 2014-05-26

* Tue Mar 04 2014 Michael Simacek <msimacek@redhat.com> - 9.0.3-8.8
- Update slf4j BR

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.3-8.7
- Mass rebuild 2014-02-19

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.3-8.6
- Rebuild to get rid of auto-requires on java-devel

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.3-8.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.3-8.4
- Remove requires on java

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.3-8.3
- Rebuild to fix incorrect auto-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.3-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.3-8.1
- First maven30 software collection build

* Fri Jan 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.3-8
- Fix typos in the changelog

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 9.0.3-7
- Mass rebuild 2013-12-27

* Wed Sep 25 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.3-6
- Clean unused conditional code
- Remove unused system-related code
- Remove jetty binary package
- Install license files with jetty-util package

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.3-5
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Jun 26 2013 Michal Srb <msrb@redhat.com> - 9.0.3-4
- Add missing BR: maven-plugin-build-helper
- Add MIT license text
- Don't install CDDL license
- More specific explanation why tests are disabled

* Wed May 29 2013 Michal Srb <msrb@redhat.com> - 9.0.3-3
- Add description for jetty-util

* Thu May 23 2013 Michal Srb <msrb@redhat.com> - 9.0.3-2
- Obsolete old jetty-websocket subpackage (Resolves: #966352)

* Thu May 09 2013 Michal Srb <msrb@redhat.com> - 9.0.3-1
- Update to upstream version 9.0.3

* Mon Apr 22 2013 Michal Srb <msrb@redhat.com> - 9.0.2-1
- Update to upstream version 9.0.2

* Thu Apr 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.0-3
- Remove maven-license-plugin
- Conditionally disable jetty-spring
- Fix OSGi conditionals

* Wed Apr 10 2013 Michal Srb <msrb@redhat.com> - 9.0.0-2
- Replace tomcat libs with glassfish libs
- Add ability to build package without service files
- Remove unneeded ecj custom depmap

* Wed Mar 13 2013 Michal Srb <msrb@redhat.com> - 9.0.0-1
- Update to upstream version 9.0.0

* Thu Mar  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.0-0.4.RC3
- Add missing BR: glassfish-el

* Mon Mar  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.0-0.3.RC3
- Update to Jetty 9 RC3

* Thu Feb 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.0-0.2.RC2
- Upload sources for Jetty 9 RC2

* Thu Feb 28 2013 Michal Srb <msrb@redhat.com> - 9.0.0-0.2.RC2
- Update to 9.0.0.RC2

* Fri Feb 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.0.0-0.1.RC0
- Remove duplicated %%files for javadoc package
- Add the new tarball to sources

* Mon Feb 18 2013 Michal Srb <msrb@redhat.com> - 9.0.0-0.1.RC0
- Update to upstream version 9.0.0
- Build with xmvn

* Fri Feb 15 2013 Alexander Kurtakov <akurtako@redhat.com> 8.1.9-3
- Add missing BR on maven-license-plugin.

* Thu Feb 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.9-2
- Update upstream URL
- Resolves: rhbz#911292

* Thu Feb 14 2013 Alexander Kurtakov <akurtako@redhat.com> 8.1.9-1
- Update to 8.1.9.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 8.1.5-11
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Dec 14 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 8.1.5-10
- Reenable osgi support

* Mon Nov  5 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 8.1.5-9
- Use file lists generated by improved add_maven_depmap macro

* Wed Oct 10 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.5-8
- Fix build conditionals

* Tue Oct  9 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.5-7
- Introduce nosql and osgi conditionals
- Temporarly disable osgi to bootstrap eclipse

* Fri Oct  5 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.5-6
- Don't delete jetty user on package erase, resolves: rhbz#857708

* Mon Aug 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.5-5
- Create work directory if not exists

* Tue Aug 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.5-4
- Convert systemd scriplets to macros, resolves #850176

* Tue Aug 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.5-3
- Don't redirect useradd and groupadd output to the bit bucket

* Tue Aug  7 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.5-2
- Put runtime data in /run instead of /tmp
- Fix patch for disabling OSGi

* Wed Jul 18 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.5-1
- Update to upstream version 8.1.5
- Fix rpmlint warnings

* Wed Jul 18 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.4-3
- Disable SPDY to fix FTBFS

* Wed Jun 13 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 8.1.4-2
- Fix jetty being accidentaly enabled after update by default
- Resolves: #831280

* Tue May 29 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.4-1
- Update to 8.1.4

* Thu May 24 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.2-9
- Add patch to disable jetty-nosql

* Wed May 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.2-8
- Build jetty-nosql conditionally

* Tue May 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.2-7
- Add unconditional BR on glassfish-jsp to make build-jar-repository work

* Wed May  9 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.2-6
- Move start.ini to /etc
- Require glassfish-jsp only for jetty-webapp and jetty-osgi
- Use shadow-utils directly instead of fedora-usermgmt-devel
- Fix license tags

* Mon Apr 30 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 8.1.2-5
- Don't require subpackages not needed by server itself
- Make jetty look for jars in correct directory
- Add proper dependent jars

* Fri Apr 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.2-4
- Keep license files only in jetty-project and jetty-javadoc packages

* Fri Apr 27 2012 Alexander Kurtakov <akurtako@redhat.com> 8.1.2-3
- There is no epoch define in jetty.

* Thu Apr 26 2012 Alexander Kurtakov <akurtako@redhat.com> 8.1.2-2
- Drop envr from jpackage-utils as it was wrong.

* Thu Apr 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 8.1.2-1
- Update to 8.1.2 upstream release

* Wed Apr 25 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.0-7
- Split into number of subpackages

* Mon Apr 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.0-6
- Drop init script, resolves #814788
- Remove jetty.script from SCM
- Reload systemd on package install/upgrade/remove

* Wed Apr 18 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8.1.0-5
- Replace eclipse-rcp BR with felix-framework
- Add missing R: felix-framework

* Fri Feb 24 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 8.1.0-4
- Add geronimo-annotation to Requires

* Thu Feb 23 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 8.1.0-3
- Fix web server running example webapp
- Add systemd unit file and conversion scriptlets

* Wed Feb 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 8.1.0-2
- Fix #794913 - missing user management utils during install

* Wed Feb  1 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 8.1.0-1
- Update to final release

* Mon Jan 30 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 8.1.0-0.4.rc5
- Fix upgrade path problems
- Symlink conf files into etc (so users still see them there)

* Thu Jan 26 2012 Alexander Kurtakov <akurtako@redhat.com> 8.1.0-0.3.rc5
- Revert the dependency on jetty-parent - we don't need the whole maven stack when installing jetty.
- Make the javadoc package not depend on the main one.

* Thu Jan 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 8.1.0-0.2.rc5
- Add jetty-parent to Requires

* Wed Jan 25 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 8.1.0-0.1.rc5
- Update to rc5
- Remove symbolic name patch (not needed after bundle plugin fix)

* Wed Jan 25 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 8.1.0-0.1.RC4
- Major update to 8.1.0 RC4
- Removed manual subpackage (was empty anyway)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 12 2011 Alexander Kurtakov <akurtako@redhat.com> 6.1.26-8
- Install jetty-client and its deps into _javadir and provide maven integration.

* Tue Jun 28 2011 Alexander Kurtakov <akurtako@redhat.com> 6.1.26-7
- Adapt build for maven 3.x.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Alexander Kurtakov <akurtako@redhat.com> 6.1.26-5
- Do not require tomcat6-lib.
- Drop one depmap.

* Tue Dec 14 2010 Alexander Kurtakov <akurtako@redhat.com> 6.1.26-4
- Do not require apache-commons-parent in order to not bring maven and friends.

* Wed Dec 01 2010 Jeff Johnston <jjohnstn@redhat.com> 6.1.26-3
- Resolves #655808
- Fix util pom to reference javax.servlet groupid for servlet-api.
- Don't add tomcat6-servlet-api to depmap.
- Remove tomcat5 BR.

* Mon Nov 22 2010 Jeff Johnston <jjohnstn@redhat.com> 6.1.26-2
- Resolves #652020
- Remove tomcat5 references and replace with appropriate alternatives.

* Fri Nov 12 2010 Alexander Kurtakov <akurtako@redhat.com> 6.1.26-1
- Update to 6.1.26.

* Tue Jun 15 2010 Alexander Kurtakov <akurtako@redhat.com> 6.1.24-1
- Update to 6.1.24.

* Wed Dec 02 2009 Jeff Johnston <jjohnstn@redhat.com> 6.1.21-4
- Resolves #543081
- Add maven depmap fragments.

* Tue Nov 03 2009 Jeff Johnston <jjohnstn@redhat.com> 6.1.21-3
- Security issues
- Resolves #532675, #5326565

* Tue Sep 29 2009 Alexander Kurtakov <akurtako@redhat.com> 6.1.21-2
- Install unversioned jars.

* Tue Sep 29 2009 Alexander Kurtakov <akurtako@redhat.com> 6.1.21-1
- Update to upstream 6.1.21 release.

* Fri Sep 18 2009 Jeff Johnston <jjohnstn@redhat.com> 6.1.20-3
- Add djetty script source and fix init script to work properly.

* Tue Sep 15 2009 Alexander Kurtakov <akurtako@redhat.com> 6.1.20-2
- Fix requires.

* Tue Sep 15 2009 Alexander Kurtakov <akurtako@redhat.com> 6.1.20-1
- Update to upstream 6.1.20.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 21 2009 Jeff Johnston <jjohnstn@redhat.com> 5.1.15-3
- Do not allow directory listings.

* Tue May 19 2009 Jeff Johnston <jjohnstn@redhat.com> 5.1.15-2
- Update OSGI manifest file.

* Tue May 19 2009 Jeff Johnston <jjohnstn@redhat.com> 5.1.15-1
- Upgrade to 5.1.15 source tarball for Fedora.

* Fri Apr 22 2009 Jeff Johnston <jjohnstn@redhat.com> 5.1.14-3
- Add %%{libdir} to files list.
- Resolves #473585

* Wed Feb 11 2009 Jeff Johnston <jjohnstn@redhat.com> 5.1.14-1.10
- Rename jettyc back to .jettyrc.
- Resolves #485012

* Tue Feb 03 2009 Jeff Johnston <jjohnstn@redhat.com> 5.1.14-1.9
- Change %%{_sysconfdir}/init.d references to be %%{_initrddir}

* Mon Feb 02 2009 Jeff Johnston <jjohnstn@redhat.com> 5.1.14-1.8
- Fixes for unowned directories.

* Tue Jan 06 2009 Jeff Johnston <jjohnstn@redhat.com> 5.1.14-1.7
- Patch init.d script to add status operation
- Patch unix djetty script so it doesn't issue error messages about /dev/tty
  and fix various inconsistencies with the init.d script

* Tue Aug 12 2008 Andrew Overholt <overholt@redhat.com> 5.1.14-1.6
- Require tomcat5 bits with proper OSGi metadata

* Fri Jul 11 2008 Andrew Overholt <overholt@redhat.com> 5.1.14-1.5
- Bump release.

* Fri Jul 11 2008 Andrew Overholt <overholt@redhat.com> 5.1.14-1.3
- Update OSGi manifest

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.1.14-1.3
- drop repotag

* Fri Jul 04 2008 Jeff Johnston <jjohnstn@redhat.com> 5.1.14-1jpp.2
- Security patch
- Resolves #417401, #417411, #417391

* Wed Jun 25 2008 Jeff Johnston <jjohnstn@redhat.com> 5.1.14-1jpp.1
- Upgrade to 5.1.14 source tarball for Fedora

* Fri Aug 31 2007 Jeff Johnston <jjohnstn@redhat.com> 5.1.12-1jpp.7
- Resolves #262221
- Use /bin/sh instead of /sbin/nologin so init will work

* Thu Aug 30 2007 Jeff Johnston <jjohnstn@redhat.com> 5.1.12-1jpp.6
- Rename all source files from jetty5 to jetty
- Replace jetty5 references with jetty in source files

* Tue Aug 28 2007 Jeff Johnston <jjohnstn@redhat.com> 5.1.12-1jpp.5
- Rename from jetty5 to jetty

* Mon Aug 27 2007 Jeff Johnston <jjohnstn@redhat.com> 5.1.12-1jpp.4
- Remove post manual step
- Remove jsse requirement
- Add comment inside jetty.conf so it isn't empty

- Use /sbin/nologin when creating the jetty5 user and group
* Mon Aug 27 2007 Jeff Johnston <jjohnstn@redhat.com> 5.1.12-1jpp.3
- Use /sbin/nologin when creating the jetty5 user and group
- Remove all jars in %%prep
- Remove unnecessary preun step for removing extra jars
- Fix license
- Fix group for manual subpackage
- Fix group for javadoc subpackage
- Add comment regarding empty jetty.conf file
- Add jsp requirement
- Remove %%post javadoc ln command
- Remove %%post manual ln command
- Change source0 tarball to remove BCLA-licensed jars
- Remove epoch 0 references in subpackage requires for extras and manual
- Rename .jettyrc to jettyrc
- Remove hidden files
- Don't install gcj files twice

* Fri Aug 24 2007 Jeff Johnston <jjohnstn@redhat.com> 5.1.12-1jpp.2
- Remove demo subpackage.

* Wed Aug 08 2007 Jeff Johnston <jjohnstn@redhat.com> 5.1.12-1jpp.1
- Comment out demo subpackage.

* Mon Aug 06 2007 Ben Konrath <bkonrath@redhat.com> 5.1.12-1jpp.1
- Add --excludes to aot-compile-rpm line.
- Inject OSGi manifest into jetty jar.

* Thu Jul 19 2007 Andrew Overholt <overholt@redhat.com> 5.1.12-1jpp.1
- Update to 5.1.12 for Fedora.
- Use fedora-usermgmt stuff.

* Fri Feb 02 2007 Ralph Apel <r.apel at r-apel.de> - 0:5.1.12-1jpp
- Upgrade to 5.1.12
- Add gcj_support option
- Avoid circular dependency with mx4j-tools thru bootstrap option

* Sat Aug 12 2006 Anthony Green <green@redhat.com> - 0:5.1.11-0.rc0.4jpp
- Escape macros in changelog with %.
- Untabify.
- Don't delete symlinks in %%preun.
- Add logrotate file.
- Don't install unversioned javadoc files.
- Don't rm old links in manual package.
- Convert some end-of-line encodings.

* Fri Aug 11 2006 Anthony Green <green@redhat.com> - 0:5.1.11-0.rc0.3jpp
- First Fedora build.
- Disable extras.
- Use fedora-useradd & fedora-userdel.
- Add gcj support.
- Tweak License and Group tags for rpmlint.
- Use full URL for Source0.

* Thu Aug 10 2006 Ralph Apel <r.apel@r-apel.de> - 0:5.1.11-0.rc0.2jpp
- Fix version/release in changelog
- Introduce option '--without extra' to omit this subpackage and its (B)Rs
- Don't delete user on erase
- Tidy up BRs
- Add commons-el.jar to ext
- No ghost for lib/org.mortbay.jetty.jar, lib/org.mortbay.jmx.jar
- Avoid use of build-jar-repository in spec
- Avoid use of rebuild-jar-repository in init and start script
- Don't handle JETTY_PID file in init script: start script takes care
- Patch PostFileFilter to remove a (unused) com.sun package import
- Explicitly (B)R  geronimo-jta-1.0.1B-api instead of any jta
- Add empty file /etc/jetty5/jetty.conf:
  activate contexts manually if desired

* Tue Jun 20 2006 Ralph Apel <r.apel@r-apel.de> - 0:5.1.2-3jpp
- First JPP-1.7 release

* Mon Mar 14 2005 Ralph Apel <r.apel@r-apel.de> - 0:5.1.2-2jpp
- link commons-logging to %%{_homedir}/ext
- link jspapi to %%{_homedir}/ext
- only use %%{_homedir}/etc not conf

* Tue Feb 01 2005 Ralph Apel <r.apel@r-apel.de> - 0:5.1.2-1jpp
- Upgrade to 5.1.2
- Prepare for build with Java 1.5, (thx to Petr Adamek)
- Require /sbin/chkconfig instead of chkconfig package

* Tue Jan 04 2005 Ralph Apel <r.apel@r-apel.de> - 0:5.0.0-2jpp
- Include build of extra, so called JettyPlus
- Create own subdirectory for jetty5 in %%{_javadir}
- Change %%{_homedir}/conf to %%{_homedir}/etc
- Dropped chkconfig requirement; just exec if /sbin/chkconfig available
- Fixed unpackaged .jettyrc

* Mon Oct 04 2004 Ralph Apel <r.apel@r-apel.de> - 0:5.0.0-1jpp
- Upgrade to 5.0.0
- Fixed URL
- relaxed some versioned dependencies

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:4.2.20-2jpp
- Rebuild with ant-1.6.2

* Fri Jun 18 2004 Ralph Apel <r.apel@r-apel.de> - 0:4.2.20-1jpp
- Upgrade to 4.2.20
- Drop ownership of /usr/share/java and /usr/bin

* Tue Feb 24 2004 Ralph Apel <r.apel@r-apel.de> - 0:4.2.17-2jpp
- enhancements and corrections thanks to Kaj J. Niemi:
- $JETTY_HOME/ext didn't exist but %%post depended on it
- correctly shutdown jetty upon uninstall
- RedHat depends on chkconfig/service to work so a functional
  init.d/jetty4 needed to be created
- djetty4 (jetty.sh) did funny things especially when it attempted to guess
  stuff
- a lot of .xml config files assumed that the configs were in etc/ instead of
  conf/

* Thu Feb 19 2004 Ralph Apel <r.apel@r-apel.de> - 0:4.2.17-1jpp
- First JPackage release.
