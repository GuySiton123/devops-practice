pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/master']],
                          doGenerateSubmoduleConfigurations: false,
                          extensions: [],
                          submoduleCfg: [],
                          userRemoteConfigs: [[url: 'https://github.com/GuySiton123/devops-practice.git',credentialsId: 'guy_github']]])
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building..."'
                sh 'docker build -t flask-app .'
            }
        }
        stage('Remove previous container') {
            steps {
                sh 'echo "Stopping and removing previous container..."'
                sh 'docker container stop flask-container'
                sh 'docker container rm flask-container'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying..."'
                sh 'docker run -d --name flask-container -p 5000:5000 flask-app'
            }
        }
    }
}
