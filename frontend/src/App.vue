<template>
  <div id="app">
    <h1>Vue Quiz App</h1>
    <quiz-flow />
  </div>
</template>

<script>
import QuizFlow from './components/QuizFlow.vue'

export default {
  name: 'App',
  components: {
    QuizFlow
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  text-align: center;
  color: #2c3e50;
}
</style> 