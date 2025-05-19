properties([
    parameters([
        string(name: 'PROXY', defaultValue: '10.128.0.1:2501', description: 'proxy to use (host:port)'),
        text(name: 'WIREGUARD_CONF', description: 'wireguard client config'),
        choice(name: 'SCRIPT_CHOICE', choices: ['simple.py', 'all_req.py'], description: 'script to run')
    ])
])

node("ec2-fleet") {

    def customImage
    def imageName = 'wireguard-client'
    def dockerfileName = 'linuxserver-custom.Dockerfile' 
    def mountDir = "${WORKSPACE}"

    stage('Clone Repo') {
        checkout scm
    }
    
    stage('Copy Wireguard Conf') {
        writeFile file: 'wireguard.conf', text: params.WIREGUARD_CONF
        sh """
            cat wireguard.conf 
        """
    }
    
    stage('Build Image') {
        customImage = docker.build("netquest/${imageName}:latest", "-f ${dockerfileName} .")
    }
    
    stage('Run Container and Test') {
        def imageTestCommand = "python /app/scripts/${params.SCRIPT_CHOICE} ${params.PROXY}"
        sh """
            set -e
            
            docker run --rm --name=wg-client \
            --cap-add=NET_ADMIN \
            -v ${WORKSPACE}/scripts:/app/scripts/ \
            -v ${WORKSPACE}/wireguard.conf:/config/wg_confs/wg0.conf \
            --sysctl='net.ipv4.conf.all.src_valid_mark=1' \
            netquest/${imageName}:latest \
            ${imageTestCommand}
        """
        sh "docker container ls -a"
    }
}
