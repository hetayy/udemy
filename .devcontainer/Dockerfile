FROM debian:13

# Create a non-root user with sudo privileges
RUN apt-get update && apt-get install -y sudo git
RUN useradd --create-home --shell /bin/bash dev
RUN usermod -aG sudo dev
RUN echo "dev ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/username

USER dev
