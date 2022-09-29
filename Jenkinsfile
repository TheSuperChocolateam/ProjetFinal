pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                git branch: 'dev', url: 'https://github.com/TheSuperChocolateam/ProjetFinal.git'
                sh 'node --version'
                sh 'svn --version'
            }
        }
    }
}
    
       
