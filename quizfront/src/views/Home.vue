<template>
  <div class="container mt-5">
    <div class="display-3 my-5 text-center">Выберете тему теста</div>
    <div class="accordion accordion-flush" id="accordionFlushExample">
      <div v-for="q in quizs" class="accordion-item">
        <h2 class="accordion-header" :id="'flush-headingOne'+q.id">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                  :data-bs-target="'#flush-collapseOne'+q.id" aria-expanded="false"
                  :aria-controls="'flush-collapseOne'+q.id">
            <h4 class="text-success">{{ q.name }}</h4>
          </button>
        </h2>
        <div :id="'flush-collapseOne'+q.id" class="accordion-collapse collapse" aria-labelledby="flush-headingOne"
             data-bs-parent="#accordionFlushExample">
          <div class="accordion-body">

            <div class="row justify-content-between  align-items-center">

              <div class="col">
                <div class="form-check form-check-inline">
                  <input v-model="quizMode" class="form-check-input" type="radio" name="inlineRadioOptions1" :id="'inlineRadio1'+q.id"
                         value="exam">
                  <label class="form-check-label" :for="'inlineRadio1'+q.id">Режим экзамена</label>
                </div>
                <div class="form-check form-check-inline">
                  <input v-model="quizMode" class="form-check-input" type="radio" name="inlineRadioOptions1" :id="'inlineRadio2'+q.id"
                         value="exercise">
                  <label class="form-check-label" :for="'inlineRadio2'+q.id">Режим тренировки</label>
                </div>
              </div>

              <div class="col">
                <span class="me-3">Количество вопросов:</span>
                <div class="form-check form-check-inline">
                  <input v-model="questionsInQuiz" class="form-check-input" type="radio" name="inlineRadioOptions2" :id="'inlineRadio3'+q.id"
                         value="10">
                  <label class="form-check-label" :for="'inlineRadio3'+q.id">10</label>
                </div>
                <div class="form-check form-check-inline">
                  <input v-model="questionsInQuiz" class="form-check-input" type="radio" name="inlineRadioOptions2" :id="'inlineRadio4'+q.id"
                         value="15">
                  <label class="form-check-label" :for="'inlineRadio4'+q.id">15</label>
                </div>
                <div class="form-check form-check-inline">
                  <input v-model="questionsInQuiz" class="form-check-input" type="radio" name="inlineRadioOptions2" :id="'inlineRadio5'+q.id"
                         value="20">
                  <label class="form-check-label" :for="'inlineRadio5'+q.id">20</label>
                </div>
              </div>

              <div class="col">
                <button @click.prevent="start(q.id)" class="btn btn-primary float-end">Начать</button>
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

const quiz = ky.create({prefixUrl: process.env.VUE_APP_PATH_SUFFIX + 'api/v1/'})
export default {
  name: 'Home',
  data: () => ({
    quizs: [],
    questionsInQuiz: 10,
    quizMode: 'exam'
  }),
  async created() {
    try {
      this.quizs = await quiz('quizs').json()
    } catch (e) {
      console.log(e)
    }
  },
  methods:{
    start(quiz_id) {
      this.$router.push({
        name: this.quizMode,
        query:{
          quiz_id, questionsInQuiz: this.questionsInQuiz
        }
      })
    }
  }
}
</script>
<style lang="scss">
</style>
