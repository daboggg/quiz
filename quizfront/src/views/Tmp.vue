<template>
  <!--  <h1>{{ test }}</h1>-->
  <!--  <button @click="aqwe">ttt</button>-->


  <div v-if="anyQuestions">
    {{ getQuest[0] }}
    <p v-for="a in getQuest[2]">
      <button @click="checkQuestion(a)"> V </button> {{a}}
    </p>
    <button
        @click="count=idx"
        :class="a"
        :disabled="Boolean(a)"
        style="margin-right: 10px"
        v-for="(a, idx) in result">
      {{ idx }}
    </button>
  </div>

  <div v-else>
    <div v-if="isWrong">
      <h1>Вы не правильно ответили на вопросы:</h1>
      <h2 v-for="(it, idx) in questions">
        {{ result[idx] === 'wrong' ? `Вопрос:  ${it[0]}  Правильный ответ: ${it[1]}` : '' }}
      </h2>
      <button @click="reset">RESET</button>
    </div>
    <div v-else>
      <h1>Вы правильно ответили на все вопросы!</h1>
      <button @click="reset">RESET</button>
    </div>
  </div>
</template>

<script>

import ky from 'ky'

const t = ky.create({prefixUrl: process.env.VUE_APP_PATH_SUFFIX + 'api/v1/'})
export default {
  name: 'Tmp',
  data: () => ({
    test: 'HUI',
    count: 0,
    questions: [
      ['Столица Кубы?', 'Гавана', ['Сеул', 'Гавана', 'Усинск']],
      ['Столица Польши?', 'Варшава', ['Варшава', 'Одесса', 'Прага']],
      ['Столица Беларуси?', 'Минск', ['Москва', 'Владивосток', 'Минск']],
      ['Столица Коми?', 'Сыктывкар', ['Парма', 'Объячево', 'Сыктывкар']],
    ],
    result: [],
  }),
  mounted() {
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
    // async aqwe() {
    //   this.test = await t('test/').json()
    // },
    checkQuestion(answer) {
      if (this.questions[this.count][1] === answer) {
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
<style lang="scss">
.wrong {
  background-color: red;
}

.correct {
  background-color: green;
}
</style>
