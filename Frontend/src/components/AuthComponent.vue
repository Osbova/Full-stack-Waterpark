<!-- <template>
    <div>
        <h2>Регистрация</h2>
        <form @submit.prevent="register">
            <div>
                <label for="registername">Имя:</label>
                <input type="text" id="registername" v-model="registername">
            </div>
            <div>
                <label for="registerAge">Кошелек:</label>
                <input type="number" id="registerWallet" v-model.number="registerwallet">
            </div>
            <div>
              <label for="Gender">Ваш пол М/Ж</label>
              <input type="text" id="gend" v-model="registerGen">
            </div>
            <button type="submit">Зарегистрироваться</button>
        </form>

        <h2>Авторизация</h2>
        <form @submit.prevent="login">
            <div>
                <label for="loginname">Имя:</label>
                <input type="text" id="loginname" v-model="loginname">
            </div>
            <button type="submit">Авторизоваться</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios';

export default {
  name: "AuthComponent",
  data() {
    return {
      registername: '',
      registerwallet: '',
      loginname: '',
      registerGen: ''
      
    }
  },
  methods: {
    async register() {
      const response = await axios.post("http://127.0.0.1:8000/User/add", {
        name: this.registername,
        wallet: Number(this.registerwallet),
        gender: this.registerGen


      });
      console.log("Register success", response.data);

    },

    async login() {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/user/${this.loginname}`);
    if (response.data) {

      this.$emit("handleAuth", response.data);
    }
  } catch (error) {
    alert("Пользователь не найден!");
  }
}
  }

}
</script>

<style scoped>   
</style> -->