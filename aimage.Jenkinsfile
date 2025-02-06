node {
    // Definición de variables de entorno
    def imageName = 'wireguard-client-existing'
    def baseImage = 'linuxserver/wireguard'
    def imageTestCommand = 'python /wgtest/main.py'
    def mountDir = "${WORKSPACE}"

    stage('Clone Repo') {
        checkout scm
    }
    
    stage('Run Container and Test') {
        // Se ejecuta el contenedor de la imagen base, se monta el directorio y se sobrescribe el comando de inicio
        sh """
            docker run --rm --cap-add=NET_ADMIN \
            -v ${mountDir}:/wgtest \
            ${baseImage}:latest \
            ${imageTestCommand}
        """
    }
}
