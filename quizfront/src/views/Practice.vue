<template>
  <div class="container">
    <!--  спиннер-->
    <div v-if="loading" class="text-center mt-5 text-primary">
      <div class="spinner-grow mt-5" role="status">
        <span class="visually-hidden">Загрузка...</span>
      </div>
    </div>

    <div v-else>
      <div>

        <h2 class="text-center my-5">Практика</h2>
        <div class="row">
          <div class="col-md-8 offset-md-2 col-xl-6 offset-xl-3">
            <div class="card shadow border-dark mx-auto">

              <div class="card-header mb-3">
                <h5>{{ getQuestion.text }}</h5>
              </div>

              <ul class="list-group list-group-flush">
                <li v-for="(a,i) in getQuestion.answers" class="list-group-item">
                  <button class="btn btn-secondary" @click="checkQuestion(a)"><span class="h5">{{ i + 1 }}</span>
                  </button>
                  <span class="h5 ms-3">{{ a.text }}</span>
                </li>
              </ul>

              <div class="card-footer text-muted">
                <button
                    @click="cursor=idx"
                    class="btn my-1"
                    :class="a ? a: 'btn-outline-secondary'"
                    style="margin-right: 10px"
                    v-for="(a, idx) in result">
                  {{ idx + 1 }}
                </button>
              </div>
              <div v-if="rightAnswer" class="card-footer text-muted">
                <p class="h5 text-success">Правильный ответ: {{ rightAnswer }}</p>
              </div>
              <div v-if="!anyQuestions" class="card-footer text-muted">
                <div class="float-end">
                  <button class="btn btn-secondary shadow me-3" @click="getQuestions">Новая тренировка</button>
                  <button class="btn btn-secondary shadow me-3" @click="$router.push('/')">Выбрать тему</button>
                  <button class="btn btn-secondary shadow" @click="reset">Еще раз</button>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import ky from "ky";
import {shuffle} from "@/utils";

const quiz = ky.create({prefixUrl: process.env.VUE_APP_PATH_SUFFIX + 'api/v1/'})
export default {
  name: "Exam",
  data: () => ({
    loading: true,
    cursor: 0,
    questions: [],
    result: [],
    rightAnswer: ''
  }),
  async created() {
    this.getQuestions()
  },
  computed: {
    getQuestion() {
      return this.questions[this.cursor]
    },
    anyQuestions() {
      return this.result.some(q => q === '')
    },
    // isWrong() {
    //   return this.result.includes('btn-danger')
    // },
    // wrongQuestions() {
    //   const res = []
    //   this.result.forEach((item, idx) => {
    //     if (item === 'btn-danger') {
    //       res.push({
    //         question: this.questions[idx].text,
    //         rightAnswer: this.questions[idx].answers.find(a => a.is_right).text
    //       })
    //     }
    //   })
    //   return res
    // }
  },
  methods: {
    checkQuestion(answer) {
      this.rightAnswer = ''
      if (answer.is_right) {
        this.result[this.cursor] = 'btn-success';
      } else {
        this.rightAnswer = this.getQuestion.answers.find(a => a.is_right).text
        this.result[this.cursor] = 'btn-danger';
      }

      // this.cursor = this.result.findIndex(item => item === '')
    },
    async getQuestions() {
      this.loading = true
      try {
        this.questions = await quiz('questions', {
          searchParams: this.$route.query
        }).json()
      } catch (e) {
        console.log(e)
      }
      this.loading = false
      this.rightAnswer = ''
      this.result = []
      this.cursor = 0
      this.questions.forEach(a => this.result.push(''))
    },
    reset() {
      this.rightAnswer = ''
      this.cursor = 0
      this.result = this.result.map(it => '')
    }
  }
}
</script>

<style scoped>
</style>