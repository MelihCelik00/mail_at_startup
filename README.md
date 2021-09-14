**Welcome to the Sending Email at Ubuntu Startup Guide**

Firstly, a systemd startup service file must be created for running the sh file.

Create a systemd unit file with .service extension in /etc/systemd/system, for example /etc/systemd/system/startup-email-service.service, with the following content. To create go into the related folder and type `sudo touch startup-email-service.service`. After creation, open it with `sudo` command to have the rights for editing.


    [Unit]
    Description=My custom startup script
    # After=network.target
    # After=systemd-user-sessions.service
    # After=network-online.target

    [Service]
    # User=spark
    # Type=simple
    # PIDFile=/run/my-service.pid
    ExecStart=~/emailSender/sendMail.sh start
    # ExecReload=~/emailSender/sendMail.sh reload
    # ExecStop=~/emailSender/sendMail.sh stop
    # TimeoutSec=30
    # Restart=on-failure
    # RestartSec=30
    # StartLimitInterval=350
    # StartLimitBurst=10

    [Install]
    WantedBy=multi-user.target

Save the file and continue to the final step.

You can now start/stop this service with `systemctl start my-service` / `systemctl stop my-service`.
To enable this service when startup, run `systemctl enable my-service`.

For the detailed information, the source is [here](https://transang.me/three-ways-to-create-a-startup-script-in-ubuntu/).
