
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
    stage('run image on remote host') { 
          env.DOCKER_HOST = 'tcp://10.1.0.11:4243' 
          docker.image('10.1.0.10:8082/mychocolateam:snapshot').inside ("-d -p 80:5501"){ "python3 /opt/apps/main.py  " } 
        //
    }
   } finally{

       cleanWs()
     }
}
    
