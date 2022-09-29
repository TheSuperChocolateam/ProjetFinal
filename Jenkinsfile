node {  
   try{
    stage('cloner le repository') {
        sh 'git clone https://github.com/TheSuperChocolateam/ProjetFinal.git' 
        sh 'cd ProjetFinal/'
        sh 'git fetch origin dev:dev'
        sh 'git checkout dev'
    }
    stage('builder le docker-compose.yaml') { 
        sh 'docker-compose up'
    }
    stage('push sur Nexus') { 
        sh echo 'titi'
    }
   } finally{
       cleanWS()
     }
}
