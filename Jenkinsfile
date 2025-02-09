pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "ant clean build"
            }
        }
        
        
        stage('Docker Build & Push') {
            steps {
                sh "docker build -t myapp:v1 ."
                sh "docker push myapp:v1"
            }
        }
        
    }
}