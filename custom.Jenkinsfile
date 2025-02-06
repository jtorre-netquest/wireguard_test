node {
    // Definición de variables de entorno
    def customImage
    def imageName = 'wireguard-client'
    def dockerfileDir = '.' // Directorio raíz, donde se encuentra el Dockerfile
    def imageTestCommand = 'python /wgtest/main.py'
    def mountDir = "${WORKSPACE}"

    stage('Clone Repo') {
        checkout scm
    }
    
    stage('Build Image') {
        // Se construye la imagen usando el Dockerfile ubicado en dockerfileDir
        customImage = docker.build("netquest/${imageName}:latest", dockerfileDir)
    }
    
    stage('Run Container and Test') {
        // Se ejecuta el contenedor, se le agrega la capacidad NET_ADMIN y se invoca el comando para ejecutar main.py
        sh "docker run --rm --privileged \
        -v ${mountDir}:/wgtest \
        netquest/${imageName}:latest ${imageTestCommand}"
    }
}

// docker run --rm --cap-add=NET_ADMIN \
//         --cap-add=SYS_MODULE \
//         -v .:/wgtest \
//         --sysctl="net.ipv4.conf.all.src_valid_mark=1"
//         test-wireguard:latest python /wgtest/main.py


//         docker run --rm --cap-add=NET_ADMIN \
//         -v .:/wgtest \
//         test-wireguard:latest python /wgtest/main.py