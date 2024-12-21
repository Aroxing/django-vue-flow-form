<template>
  <flow-form
    v-if="questions.length"
    :questions="flowQuestions"
    @complete="onComplete"
    :language="language"
  >
    <template #complete>
      <div class="f-section-wrap">
        <p>Quiz completed! Your score: {{ score }}/{{ questions.length }}</p>
      </div>
    </template>
  </flow-form>
</template>

<script>
import {FlowForm, QuestionModel, QuestionType, ChoiceOption, LanguageModel} from '@ditdot-dev/vue-flow-form'
import axios from 'axios'

export default {
  name: 'QuizFlow',
  components: {
    FlowForm
  },
  data() {
    return {
      questions: [],
      score: 0,
      language: new LanguageModel()
    }
  },
  computed: {
    flowQuestions() {
      return this.questions.map(q => new QuestionModel({
        id: `q_${q.id}`,
        title: q.text,
        type: this.mapQuestionType(q.question_type),
        required: true,
        multiple: false,
        options: q.answers.map(a => new ChoiceOption({
          label: a.text,
          value: a.text,
          score: a.is_correct ? 1 : 0
        }))
      }))
    }
  },
  methods: {
    mapQuestionType(type) {
      const typeMap = {
        'text': QuestionType.Text,
        'multiple': QuestionType.MultipleChoice,
        'boolean': QuestionType.MultipleChoice
      }
      return typeMap[type] || QuestionType.MultipleChoice
    },
    async fetchQuestions() {
      try {
        const response = await axios.get('http://localhost:8000/api/questions/')
        this.questions = response.data
      } catch (error) {
        console.error('Error fetching questions:', error)
      }
    },
    onComplete(completed, questionList) {
      this.score = questionList.reduce((total, q) => {
        const selectedOption = q.options?.find(o => o.selected)
        return total + (selectedOption?.score || 0)
      }, 0)
    }
  },
  mounted() {
    this.fetchQuestions()
  }
}
</script>

<style>
@import '@ditdot-dev/vue-flow-form/dist/vue-flow-form.css';
</style> 