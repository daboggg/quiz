<template>
  <div v-if="loading">XXXXXXXXXXXXXXXXXXXXXXX</div>
  <div v-else>
    <div v-if="anyQuestions">
      <!--<h1>{{params}}</h1>-->
      <!--<h1>{{questions}}</h1>-->
      {{ getQuest.text }}

      <p v-for="a in getQuest.answers">
        <button @click="checkQuestion(a)"> V</button>
        {{ a.text }}
      </p>

      <button
          @click="count=idx"
          :class="a"
          :disabled="Boolean(a)"
          style="margin-right: 10px"
          v-for="(a, idx) in result">
        {{ idx +1 }}
      </button>

      {{ result }}
    </div>
    <div v-else>
      <div v-if="isWrong">
        <h1>Вы не правильно ответили на вопросы:</h1>
        <h2 v-for="(it, idx) in questions">
          {{ result[idx] === 'wrong' ? `Вопрос:  ${it.text}  Правильный ответ: ${it.answers.find(a=> a.is_right).text}` : '' }}
        </h2>
        <button @click="reset">RESET</button>
      </div>
      <div v-else>
        <h1>Вы правильно ответили на все вопросы!</h1>
        <button @click="reset">RESET</button>
      </div>
    </div>
  </div>
</template>

<script>
import ky from "ky";

const quiz = ky.create({prefixUrl: process.env.VUE_APP_PATH_SUFFIX + 'api/v1/'})
export default {
  name: "Exam",
  data: () => ({
    loading: true,
    params: null,
    count: 0,
    questions: {},
    result: [],
  }),
  async created() {
    this.params = this.$route.query
    try {
      this.questions = await quiz('questions', {
        searchParams: this.params
      }).json()
    } catch (e) {
      console.log(e)
    }
    this.loading = false
    this.questions.forEach(a => this.result.push(''))
  },
  computed: {
    getQuest() {
      return this.questions[this.count]
    },
    anyQuestions() {
      return this.result.some(q => q === '')
    },
    isWrong() {
      return this.result.includes('wrong')
    }
  },
  methods: {
    checkQuestion(answer) {
      if (answer.is_right) {
        this.result[this.count] = 'correct';
      } else {
        this.result[this.count] = 'wrong';
      }

      this.count = this.result.findIndex(item => item === '')
    },
    reset() {
      this.count = 0
      this.result = this.result.map(it => '')
    }
  }
}
</script>

<style scoped>
.wrong {
  background-color: red;
}

.correct {
  background-color: green;
}
</style>