#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cloud-native-setup
Version  : 1.5
Release  : 6
URL      : https://github.com/clearlinux/cloud-native-setup/archive/v1.5.tar.gz
Source0  : https://github.com/clearlinux/cloud-native-setup/archive/v1.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: cloud-native-setup-data = %{version}-%{release}
Requires: cloud-native-setup-license = %{version}-%{release}

%description
# How to setup the cluster
## Prerequisite
This setup currently will work with k8s 1.14 & above. Any version of k8s before that might work, but is not guaranteed.

%package data
Summary: data components for the cloud-native-setup package.
Group: Data

%description data
data components for the cloud-native-setup package.


%package license
Summary: license components for the cloud-native-setup package.
Group: Default

%description license
license components for the cloud-native-setup package.


%prep
%setup -q -n cloud-native-setup-1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559674976
export GCC_IGNORE_WERROR=1
export LDFLAGS="${LDFLAGS} -fno-lto"
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1559674976
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cloud-native-setup
cp LICENSE %{buildroot}/usr/share/package-licenses/cloud-native-setup/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/clr-k8s-examples/0-canal/canal.yaml
/usr/share/clr-k8s-examples/0-canal/rbac.yaml
/usr/share/clr-k8s-examples/0-canal/versions
/usr/share/clr-k8s-examples/1-core-metrics/aggregated-metrics-reader.yaml
/usr/share/clr-k8s-examples/1-core-metrics/auth-delegator.yaml
/usr/share/clr-k8s-examples/1-core-metrics/auth-reader.yaml
/usr/share/clr-k8s-examples/1-core-metrics/metrics-apiservice.yaml
/usr/share/clr-k8s-examples/1-core-metrics/metrics-server-deployment.yaml
/usr/share/clr-k8s-examples/1-core-metrics/metrics-server-service.yaml
/usr/share/clr-k8s-examples/1-core-metrics/resource-reader.yaml
/usr/share/clr-k8s-examples/1-core-metrics/versions
/usr/share/clr-k8s-examples/2-dashboard/dashboard-admin.yaml
/usr/share/clr-k8s-examples/2-dashboard/kubernetes-dashboard.yaml
/usr/share/clr-k8s-examples/2-dashboard/versions
/usr/share/clr-k8s-examples/3-efk/es-service.yaml
/usr/share/clr-k8s-examples/3-efk/es-statefulset.yaml
/usr/share/clr-k8s-examples/3-efk/fluentd-es-configmap.yaml
/usr/share/clr-k8s-examples/3-efk/fluentd-es-ds.yaml
/usr/share/clr-k8s-examples/3-efk/fluentd-es-image/Dockerfile
/usr/share/clr-k8s-examples/3-efk/fluentd-es-image/Gemfile
/usr/share/clr-k8s-examples/3-efk/fluentd-es-image/Makefile
/usr/share/clr-k8s-examples/3-efk/fluentd-es-image/README.md
/usr/share/clr-k8s-examples/3-efk/fluentd-es-image/clean-apt
/usr/share/clr-k8s-examples/3-efk/fluentd-es-image/clean-install
/usr/share/clr-k8s-examples/3-efk/fluentd-es-image/fluent.conf
/usr/share/clr-k8s-examples/3-efk/fluentd-es-image/run.sh
/usr/share/clr-k8s-examples/3-efk/kibana-deployment.yaml
/usr/share/clr-k8s-examples/3-efk/kibana-service.yaml
/usr/share/clr-k8s-examples/3-efk/versions
/usr/share/clr-k8s-examples/4-kube-prometheus/00namespace-namespace.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/0prometheus-operator-0alertmanagerCustomResourceDefinition.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/0prometheus-operator-0prometheusCustomResourceDefinition.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/0prometheus-operator-0prometheusruleCustomResourceDefinition.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/0prometheus-operator-0servicemonitorCustomResourceDefinition.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/0prometheus-operator-clusterRole.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/0prometheus-operator-clusterRoleBinding.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/0prometheus-operator-deployment.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/0prometheus-operator-service.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/0prometheus-operator-serviceAccount.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/0prometheus-operator-serviceMonitor.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/alertmanager-alertmanager.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/alertmanager-secret.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/alertmanager-service.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/alertmanager-serviceAccount.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/alertmanager-serviceMonitor.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/grafana-dashboardDatasources.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/grafana-dashboardDefinitions.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/grafana-dashboardSources.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/grafana-deployment.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/grafana-service.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/grafana-serviceAccount.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/kube-state-metrics-clusterRole.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/kube-state-metrics-clusterRoleBinding.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/kube-state-metrics-deployment.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/kube-state-metrics-role.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/kube-state-metrics-roleBinding.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/kube-state-metrics-service.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/kube-state-metrics-serviceAccount.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/kube-state-metrics-serviceMonitor.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/node-exporter-clusterRole.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/node-exporter-clusterRoleBinding.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/node-exporter-daemonset.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/node-exporter-service.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/node-exporter-serviceAccount.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/node-exporter-serviceMonitor.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-clusterRole.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-clusterRoleBinding.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-prometheus.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-roleBindingConfig.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-roleBindingSpecificNamespaces.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-roleConfig.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-roleSpecificNamespaces.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-rules.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-service.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-serviceAccount.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-serviceMonitor.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-serviceMonitorApiserver.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-serviceMonitorCoreDNS.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-serviceMonitorKubeControllerManager.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-serviceMonitorKubeScheduler.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/prometheus-serviceMonitorKubelet.yaml
/usr/share/clr-k8s-examples/4-kube-prometheus/versions
/usr/share/clr-k8s-examples/5-ingres-lb/mandatory.yaml
/usr/share/clr-k8s-examples/5-ingres-lb/service-nodeport.yaml
/usr/share/clr-k8s-examples/5-ingres-lb/versions
/usr/share/clr-k8s-examples/6-metal-lb/example-layer2-config.yaml
/usr/share/clr-k8s-examples/6-metal-lb/metallb.yaml
/usr/share/clr-k8s-examples/6-metal-lb/versions
/usr/share/clr-k8s-examples/7-rook/000-operator.yaml
/usr/share/clr-k8s-examples/7-rook/001-cluster.yaml
/usr/share/clr-k8s-examples/7-rook/002-storageclass.yaml
/usr/share/clr-k8s-examples/7-rook/update.sh
/usr/share/clr-k8s-examples/8-kata/deploy/kata-cleanup.yaml
/usr/share/clr-k8s-examples/8-kata/deploy/kata-deploy.yaml
/usr/share/clr-k8s-examples/8-kata/deploy/kata-rbac.yaml
/usr/share/clr-k8s-examples/8-kata/kata-fc-runtimeClass.yaml
/usr/share/clr-k8s-examples/8-kata/kata-qemu-runtimeClass.yaml
/usr/share/clr-k8s-examples/9-multi-network/Dockerfile
/usr/share/clr-k8s-examples/9-multi-network/README.md
/usr/share/clr-k8s-examples/9-multi-network/cni/vfioveth
/usr/share/clr-k8s-examples/9-multi-network/multus-sriov-ds.yaml
/usr/share/clr-k8s-examples/9-multi-network/sriov-conf.yaml
/usr/share/clr-k8s-examples/9-multi-network/systemd/sriov.service
/usr/share/clr-k8s-examples/9-multi-network/systemd/sriov.sh
/usr/share/clr-k8s-examples/9-multi-network/test/bridge/0-bridge-net.yaml
/usr/share/clr-k8s-examples/9-multi-network/test/bridge/1-pod-bridge.yaml
/usr/share/clr-k8s-examples/9-multi-network/test/pod.yaml
/usr/share/clr-k8s-examples/9-multi-network/test/sriov/0-sriov-net.yaml
/usr/share/clr-k8s-examples/9-multi-network/test/sriov/1-pod-sriov.yaml
/usr/share/clr-k8s-examples/README.md
/usr/share/clr-k8s-examples/Vagrantfile
/usr/share/clr-k8s-examples/admit-kata/README.md
/usr/share/clr-k8s-examples/admit-kata/create-certs.sh
/usr/share/clr-k8s-examples/admit-kata/deploy/webhook-registration.yaml.tpl
/usr/share/clr-k8s-examples/admit-kata/deploy/webhook.yaml
/usr/share/clr-k8s-examples/admit-kata/versions
/usr/share/clr-k8s-examples/create_stack.sh
/usr/share/clr-k8s-examples/kubeadm.yaml
/usr/share/clr-k8s-examples/reset_stack.sh
/usr/share/clr-k8s-examples/setup_kata_firecracker.sh
/usr/share/clr-k8s-examples/setup_system.sh
/usr/share/clr-k8s-examples/tests/autoscale/load-gen.yaml
/usr/share/clr-k8s-examples/tests/autoscale/php.yaml
/usr/share/clr-k8s-examples/tests/autoscale/test-autoscale.sh
/usr/share/clr-k8s-examples/tests/cpumanager/test-cpumanager.sh
/usr/share/clr-k8s-examples/tests/cpumanager/test-cpumanager.yaml.tmpl
/usr/share/clr-k8s-examples/tests/deploy-svc-ing/test-deploy-kata-fc.yaml
/usr/share/clr-k8s-examples/tests/deploy-svc-ing/test-deploy-kata-qemu.yaml
/usr/share/clr-k8s-examples/tests/deploy-svc-ing/test-deploy-runc.yaml
/usr/share/clr-k8s-examples/tests/deploy-svc-ing/test-ingress-kata.yaml
/usr/share/clr-k8s-examples/tests/deploy-svc-ing/test-ingress-runc.yaml
/usr/share/clr-k8s-examples/tests/pvc/wordpress.yaml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cloud-native-setup/LICENSE
