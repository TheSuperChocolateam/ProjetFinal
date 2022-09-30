
node {  
   try{
    stage('cloner le repository') {
        git branch: 'dev', url: 'https://github.com/TheSuperChocolateam/ProjetFinal.git'
        sh 'whoami'
    }
    stage('builder le docker-compose.yaml') { 
          def myEnv = docker.build '10.1.0.10:8082/mychocolateam:snapshot'
          myEnv.push() // record this snapshot (optional)
    }
    stage('push sur Nexus') { 
          
        sh 'echo coucou'
    }
   } finally{

       cleanWs()
     }
}
    
