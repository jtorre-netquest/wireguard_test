properties([
    parameters([
        text(name: 'WIREGUARD_CONF', description: 'wireguard client config'),
        choice(name: 'SCRIPT_CHOICE', choices: ['simple.py', 'all_req.py'], description: 'script to run')
    ])
])

node("ubuntu24-fleet") {

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
        def imageTestCommand = "python /app/scripts/${params.SCRIPT_CHOICE}"
        sh """
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
