
node {  
   try{
    stage('cloner le repository') {
        git branch: 'dev', url: 'https://github.com/TheSuperChocolateam/ProjetFinal.git'
    }
    stage('builder le docker-compose.yaml') { 
          def myEnv = docker.build 'my-environment:snapshot'
    }
    stage('push sur Nexus') { 
        sh echo 'titi'
    }
   } finally{

       cleanWs()
     }
}
    
