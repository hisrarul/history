variable "AWS_ACCESS_KEY" {

}
variable "AWS_SECRET_KEY" {

}
variable "AWS_REGION" {
  default = "us-east-1"
}

variable "INSTANCE_TYPE" {
  default = "t2.micro"
}

variable "INSTANCE_DEVICE_NAME" {
  default = "/dev/xvdb"
}

variable "KEY_NAME" {
  type = string
  description = "Enter the name of keypair"
}