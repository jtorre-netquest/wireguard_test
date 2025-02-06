node {
    // Definición de variables de entorno
    def imageName = 'wireguard-client-existing'
    def baseImage = 'lscr.io/linuxserver/wireguard'
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

        docker run -rm \
  --name=wireguard-client \
  --cap-add=NET_ADMIN \
  --cap-add=SYS_MODULE `#optional` \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -p 51820:51820/udp \
  -v wireguard.conf:/config/wg_confs/wg0.conf \
  
  --sysctl="net.ipv4.conf.all.src_valid_mark=1" \
  lscr.io/linuxserver/wireguard:latest
    }
}
