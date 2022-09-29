
node {  
   try{
    stage('cloner le repository') {
        git branch: 'dev', url: 'https://github.com/TheSuperChocolateam/ProjetFinal.git'
        sh 'whoami'
    }
    stage('builder le docker-compose.yaml') { 
          def myEnv = docker.build '10.1.0.10:8082/my-environment:snapshot'
    }
    stage('push sur Nexus') { 
          myEnv.push() // record this snapshot (optional)

    }
   } finally{

       cleanWs()
     }
}
    
