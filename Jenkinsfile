
node {  
   try{
    stage('cloner le repository') {
        git branch: 'dev', url: 'https://github.com/TheSuperChocolateam/ProjetFinal.git'
    }
    stage('builder le docker-compose.yaml') { 
        sh 'ls -la'
    }
    stage('push sur Nexus') { 
        sh echo 'titi'
    }
   } finally{

       cleanWS()
     }
}
    
