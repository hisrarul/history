resource "aws_instance" "lamp-server" {
  ami           = "ami-02eac2c0129f6376b"
  instance_type = "${var.INSTANCE_TYPE}"
  vpc_security_group_ids = ["${aws_security_group.allow_http.id}"]
  availability_zone = "us-east-1a"
  key_name = "${var.KEY_NAME}"

  user_data = <<-EOF
		#! /bin/bash
        cd /tmp
        sudo yum install git -y
		git clone https://hisrarul@bitbucket.org/hisrarul/assignment.git
        sudo chmod +x /tmp/assignment/assignment5/lamp.sh
        sudo sh /tmp/assignment/assignment5/lamp.sh Y | sudo tee -a /tmp/log.txt
        EOF
  tags = {
    Name = "lamp-server-wordpress"
  }
}

resource "aws_ebs_volume" "ebs-data-volume1" {
    availability_zone = "us-east-1a"
    size = 15
    type = "gp2"
}

resource "aws_volume_attachment" "ebs-data-volume1-attachment" {
  device_name = "${var.INSTANCE_DEVICE_NAME}"
  volume_id = "${aws_ebs_volume.ebs-data-volume1.id}"
  instance_id = "${aws_instance.lamp-server.id}"
}

resource "aws_security_group" "allow_http" {
  name        = "allow_http"
  description = "Allow HTTP inbound traffic"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }
}