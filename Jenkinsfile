pipeline {
  agent any
  parameters {
    gitParameter branchFilter: 'origin/(.*)', defaultValue: 'dev', name: 'BRANCH', type: 'PT_BRANCH'
  }
  stages {
    stage('Example') {
      steps {
        git branch: "${params.BRANCH}", url: 'https://github.com/TheSuperChocolateam/ProjetFinal.git'
      }
    }
  }
}