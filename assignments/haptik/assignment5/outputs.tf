output "instanceId" {
  value = "${aws_instance.lamp-server.id}"
}

output "publicip" {
  value = "${aws_instance.lamp-server.public_ip}"
}