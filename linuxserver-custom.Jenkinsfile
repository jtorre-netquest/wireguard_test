node {

    def customImage
    def imageName = 'wireguard-client'
    def dockerfileName = 'linuxserver-custom.Dockerfile' 
    def imageTestCommand = 'python /app/main.py'
    def mountDir = "${WORKSPACE}"

    stage('Clone Repo') {
        checkout scm
    }
    
    stage('Build Image') {
        customImage = docker.build("netquest/${imageName}:latest", "-f ${dockerfileName} .")
    }
    
    stage('Run Container and Test') {
        sh "docker run --name=wg-client \
            --cap-add=NET_ADMIN \
            --network=wireguard-net \
            -v ./wireguard.conf:/config/wg_confs/wg0.conf \
            -v ./main.py:/app/main.py \
            --sysctl="net.ipv4.conf.all.src_valid_mark=1" \
            netquest/${imageName}:latest \
            ${imageTestCommand}"
        
    }
}