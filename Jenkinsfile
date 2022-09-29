
node {  
   try{
    stage('cloner le repository') {
        git branch: 'dev', url: 'https://github.com/TheSuperChocolateam/ProjetFinal.git'
    }
    stage('builder le docker-compose.yaml') { 
        sh 'echo tata'
    }
    stage('push sur Nexus') { 
        sh echo 'titi'
    }
   } finally{

       cleanWS()
     }
}
    
