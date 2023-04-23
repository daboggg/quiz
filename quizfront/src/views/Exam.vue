<template>
  <div class="container">
    <!--  спиннер-->
    <div v-if="loading" class="text-center mt-5 text-primary">
      <div class="spinner-grow mt-5" role="status">
        <span class="visually-hidden">Загрузка...</span>
      </div>
    </div>

    <div v-else>
      <div v-if="anyQuestions">


        <div class="row mt-5">
          <div class="col-md-8 offset-md-2 col-xl-6 offset-xl-3">
            <div class="card border-dark mx-auto">

              <div class="card-header mb-3">
                <h5>{{ getQuest.text }}</h5>
              </div>

              <ul class="list-group list-group-flush">
                <li v-for="(a,i) in getQuest.answers" class="list-group-item">
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
                    :disabled="Boolean(a)"
                    style="margin-right: 10px"
                    v-for="(a, idx) in result">
                  {{ idx + 1 }}
                </button>
              </div>
            </div>
          </div>
        </div>

      </div>

      <div v-else>

        <div class="row">
          <div class="col-md-8 offset-md-2 col-xl-6 offset-xl-3">

            <div v-if="wrongQuestions.length">
              <h2 class="text-center my-5">Вы не правильно ответили на вопросы:</h2>
              <table class="table table-success table-striped table-bordered border-dark  align-middle">
                <thead class="table-dark">
                <tr>
                  <th><span class="h4">Вопрос</span></th>
                  <th><span class="h4">Правильный ответ</span></th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="item in wrongQuestions">
                  <td><span class="h5">{{ item.question }}</span></td>
                  <td><span class="h5">{{ item.rightAnswer }}</span></td>
                </tr>
                </tbody>
              </table>
              <!--              <h2 class="text-center">Вы не правильно ответили на вопросы:</h2>-->
              <!--              <h5 v-for="item in wrongQuestions">-->
              <!--                {{-->
              <!--                `Вопрос: ${item.question} Правильный ответ: ${item.rightAnswer}`-->
              <!--                }}-->
              <!--              </h5>-->

              <div class="float-end">
                <button class="btn btn-secondary me-3" @click="$router.push('/')">Выбрать тему</button>
                <button class="btn btn-secondary" @click="reset">Еще раз</button>
              </div>
            </div>
            <div v-else>
              <h1 class="text-center">Поздравляем вы правильно ответили на все вопросы!</h1>
              <button @click="reset">RESET</button>
            </div>
          </div>
        </div>
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
    cursor: 0,
    questions: {},
    result: [],
  }),
  async created() {
    this.params = this.$route.query
    try {
      this.questions = await quiz('questions', {
        searchParams: this.$route.query
      }).json()
    } catch (e) {
      console.log(e)
    }
    this.loading = false
    this.questions.forEach(a => this.result.push(''))
  },
  computed: {
    getQuest() {
      return this.questions[this.cursor]
    },
    anyQuestions() {
      return this.result.some(q => q === '')
    },
    isWrong() {
      return this.result.includes('btn-danger')
    },
    wrongQuestions() {
      const res = []
      this.result.forEach((item, idx) => {
        if (item === 'btn-danger') {
          res.push({
            question: this.questions[idx].text,
            rightAnswer: this.questions[idx].answers.find(a => a.is_right).text
          })
        }
      })
      return res
    }
  },
  methods: {
    checkQuestion(answer) {
      if (answer.is_right) {
        this.result[this.cursor] = 'btn-success';
      } else {
        this.result[this.cursor] = 'btn-danger';
      }

      this.cursor = this.result.findIndex(item => item === '')
    },
    reset() {
      this.cursor = 0
      this.result = this.result.map(it => '')
    }
  }
}
</script>

<style scoped>
/*.wrong {*/
/*  background-color: red;*/
/*}*/

/*.correct {*/
/*  background-color: green;*/
/*}*/
</style>