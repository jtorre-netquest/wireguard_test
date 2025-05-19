# create a readme that explains all the repo
# Wireguard Client Testing Environment

This repository contains Docker-based testing environments for Wireguard VPN clients. It provides two different implementations using different base images and configurations.

## Overview

The repository includes:
- Docker configurations for Wireguard client testing
- Jenkins pipeline configurations for automated testing
- Custom Docker images based on both Ubuntu and LinuxServer.io Wireguard images
- Testing scripts for VPN connectivity

## Components

### Docker Images

1. **Ubuntu-based Image** (`ubuntu-custom.Dockerfile`)
   - Based on Python 3.13 slim image
   - Includes Wireguard tools and necessary networking utilities
   - Configured with a non-root user for security
   - Uses `wg-quick` for Wireguard interface management

2. **LinuxServer-based Image** (`linuxserver-custom.Dockerfile`)
   - Based on LinuxServer.io's Wireguard image
   - Includes Python and additional utilities
   - Maintains compatibility with LinuxServer.io's Wireguard implementation

### Jenkins Pipelines

1. **Ubuntu Pipeline** (`ubuntu-custom.Jenkinsfile`)
   - Builds and tests the Ubuntu-based image
   - Configurable parameters for proxy settings and Wireguard configuration
   - Supports different test script options

2. **LinuxServer Pipeline** (`linuxserver-custom.Jenkinsfile`)
   - Similar to Ubuntu pipeline but for LinuxServer-based image
   - Different configuration paths for Wireguard

### Testing Scripts

- `simple.py`: Basic connectivity test
- `all_req.py`: Comprehensive request testing

## Local Testing

There is a folder with local confs for testing in two containers for server and client of wireguard.

Also a file with usefull commands for local testing




