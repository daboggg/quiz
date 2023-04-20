<template>
  <h1>{{ test }}</h1>
  <button @click="aqwe">ttt</button>
</template>

<script>

import ky from 'ky'
const t = ky.create({prefixUrl: process.env.VUE_APP_PATH_SUFFIX + 'api/v1/'})
export default {
  name: 'HomeView',
  data:()=>({
    test:'HUI'
  }),
  async mounted() {

  },
  methods:{
    async aqwe() {
      this.test = await t('test/').json()
    }
  }
}
</script>
