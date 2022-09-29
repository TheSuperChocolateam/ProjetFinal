node {  
   try{
    stage('cloner le repository') {
        sh 'git clone https://github.com/TheSuperChocolateam/ProjetFinal.git' 
        sh 'cd ProjetFinal/'
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
