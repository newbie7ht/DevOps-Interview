provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"  # Example AMI ID
  instance_type = "t2.micro"

  tags = {
    Name = "TerraformExample"
  }

  # Define a security group to allow SSH access
  vpc_security_group_ids = ["sg-0a1b2c3d4e5f67890"]

  key_name = "your-key-pair-name"

  # Add user data to run a script on instance creation
  user_data = <<-EOF
              #!/bin/bash
              echo "Hello, World!" > /var/www/html/index.html
              EOF
}

output "instance_ip" {
  value = aws_instance.example.public_ip
}
