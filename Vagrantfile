Vagrant.configure("2") do |config|
  # https://portal.cloud.hashicorp.com/vagrant/discover
  #config.vm.box = "generic/rhel9" # issue with libxml2-devel needed for PHP
  #config.vm.box = "generic/fedora39"
  #config.vm.box = "fedora/41-cloud-base"
  #config.vm.box = "generic/rhel8"
  #config.vm.box = "generic/centos9s"
  #config.vm.box = "generic/oracle9"
  #config.vm.box = "generic/oracle8"
  #config.vm.box = "generic/rocky9"
  config.vm.box = "generic/alma9"
  #config.vm.box = "generic/ubuntu2204"
  #config.vm.box = "ubuntu/jammy64"
  #config.vm.box = "generic/debian12"
  #config.vm.box = "generic/openbsd7"
  #config.vm.box = "generic/netbsd9"
  #config.vm.box = "generic/freebsd14"
  #config.vm.box = "generic/alpine319"
  #config.vm.box = "generic/opensuse42"
  #config.vm.box = "debian/bookworm64"

  config.vm.define "machine1"
  #config.vm.synced_folder '.vagrant/scripts', '/home/vagrant/scripts'
  #config.vm.provision :shell, path: ".vagrant/bootstrap.sh"

  #config.vm.hostname = "myhost.local"
  config.vm.network "public_network"
  #config.vm.network "forwarded_port", guest: 80, host: 8000

  #config.ssh.insert_key = false

  #config.hostmanager.enabled = true

  #
  # Run Ansible from the Vagrant Host
  #
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/main.yml"
    ansible.verbose = true
    ansible.groups = {
      "web" => ["machine1"],
      "database" => ["machine1"],
    }
  end

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 2
  end
end