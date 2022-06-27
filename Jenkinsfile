pipeline{
    agent any 
    environment{
        dockerhub = credentials("dockerhub_luna4444")
    }

    stages {
        stage('Build Image'){
            steps{
                sh 'docker build -t todo_app_jenkins .'
            }
    }
    stage("Start Pushing to Docker Hub"){
            steps {
            sh 'docker push todo_app_jenkins'
            sh 'echo $dockerhub_PSW | docker login -u $dockerhub_USR --password-stdin'

            sh 'docker push $dockerhub_USR/todo_app_jenkins'
            }
    }

    }
    
}