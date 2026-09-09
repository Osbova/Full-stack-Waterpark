<template>
  <div class="admin-page">
    <header class="admin-header">
      <div class="header-left">
        <span class="admin-badge">ADMIN</span>
        <h1>Панель управления</h1>
      </div>
      <router-link to="/menu" class="back-link">← Вернуться на сайт</router-link>
    </header>

    <div class="admin-layout">
      <aside class="sidebar">
        <button
          class="nav-tab"
          :class="{ active: activeTab === 'tickets' }"
          @click="activeTab = 'tickets'"
        >
          Билеты
        </button>
        <button
          class="nav-tab"
          :class="{ active: activeTab === 'food' }"
          @click="activeTab = 'food'"
        >
          Еда / Меню
        </button>
        <button
          class="nav-tab"
          :class="{ active: activeTab === 'users' }"
          @click="activeTab = 'users'"
        >
          Пользователи
        </button>
      </aside>

      <main class="content-area">
        <div v-if="activeTab === 'tickets'" class="tab-panel">
          <div class="panel-header">
            <h2>Управление билетами</h2>
            <p class="subtitle">Просмотр и добавление категорий билетов</p>
          </div>

          <div class="grid-container">
            <div class="card form-card">
              <h3>Добавить билет</h3>
              <div class="form-group">
                <label>Название билета</label>
                <input
                  type="text"
                  placeholder="Например: Взрослый"
                  class="custom-input"
                  v-model="Tickettitle"
                />
              </div>
              <div class="form-group">
                <label>Цена (₽)</label>
                <input type="number" placeholder="3590" class="custom-input" v-model="Ticketprice" />
              </div>
              <div class="form-group">
                <label>Количество в наличии</label>
                <input type="number" placeholder="100" class="custom-input" v-model="Ticketcol" />
              </div>
              <button class="primary-btn" @click="AddTicket">Сохранить билет</button>
            </div>

            <div class="card table-card">
              <h3>Список билетов</h3>
              <table class="styled-table">
                <thead>
                  <tr>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Количество</th>
                    <th>Id</th>
                    <th>Админ</th>
                    <th>Действия</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="it in ticket" :key="it.id">
                    <td>{{ it.title }}</td>
                    <td>{{ it.price }} ₽</td>
                    <td>{{ it.col }}</td>
                    <td>{{ it.id }}</td>
                    <td>{{ it.creator?.name || "Не указан" }} id -> {{ it.creator.id }}</td>
                    <td>
                      <button 
                        @click="deleteTicket(it.id)" 
                        class="btn-delete"
                      >
                        Удалить
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <div v-if="activeTab === 'food'" class="tab-panel">
          <div class="panel-header">
            <h2>Меню и Питание</h2>
            <p class="subtitle">Добавление позиций в меню аквапарка</p>
          </div>

          <div class="grid-container">
            <div class="card form-card">
              <h3>Добавить блюдо</h3>
              <div class="form-group">
                <label>Название</label>
                <input
                  type="text"
                  placeholder="Пицца Пепперони"
                  class="custom-input"
                  v-model="Foodtitle"

                />
              </div>
              <div class="form-group">
                <label>Особенности</label>
                <input
                  type="text"
                  placeholder="Острая, с соусом"
                  class="custom-input" 
                  v-model="Foodtaste"
                />
              </div>
              <div class="form-group">
                <label>Цена (₽)</label>
                <input type="number" placeholder="650" class="custom-input" v-model="Foodprice" />
              </div>
              <button class="primary-btn"  @click="AddFood">Добавить в меню</button>
            </div>

            <div class="card table-card">
              <h3>Все позиции</h3>
              <table class="styled-table">
                <thead>
                  <tr>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Id</th>
                    <th>Админ</th>
                    <th>Действия</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="it in food" :key="it.id">
                    <td>{{ it.name }}</td>
                    <td>{{ it.price }} ₽</td>
                    <td>{{ it.id }}</td>
                    <td>{{ it.creator?.name || "Не указан" }} id -> {{ it.creator.id }}</td>
                    <td>
                      <button 
                        @click="deleteFood(it.id)" 
                        class="btn-delete"
                      >
                        Удалить
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <div v-if="activeTab === 'users'" class="tab-panel">
          <div class="panel-header">
            <h2>Пользователи</h2>
            <p class="subtitle">Управление зарегистрированными аккаунтами</p>
          </div>

          <div class="card table-card">
            <table class="styled-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Имя</th>
                  <th>Роль</th>
                  <th>Действия</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="it in user" :key="it.id">
                  <td>{{ it.id }}</td>
                  <td>{{ it.name }}</td>
                  <td>
                    <select
                      :value="it.role"
                      @change="changeRole(it.id, $event.target.value)"
                      class="role-select"
                      :class="it.role ? it.role.toLowerCase() : 'user'"
                      :disabled="it.role === 'owner'"
                    >
                      <option value="user" class="opt-user">user</option>
                      <option value="employee" class="opt-employee">employee</option>
                      <option value="waiter" class="opt-waiter">waiter</option>
                      <option value="admin" class="opt-admin">admin</option>
                      <option value="owner" class="opt-owner" disabled>owner</option>
                    </select>
                  </td>
                  <td>
                    <button 
                      @click="deleteUser(it.id)" 
                      class="btn-delete"
                      :disabled="it.role === 'owner'"
                    >
                      Удалить
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const activeTab = ref("tickets");
const Tickettitle = ref("")
const Ticketprice = ref("")
const Ticketcol = ref("")
const Foodtitle = ref("")
const Foodtaste = ref("")
const Foodprice = ref("")
const currentAdminId = ref(1);

async function AddFood(){
  if (Foodprice.value !== "" && Foodtaste.value !== "" && Foodtitle !== ""){
    const Foodata = {
      name: Foodtitle.value,
      price: Foodprice.value,
      taste: Foodtaste.value,
      user_id: currentAdminId.value
    }
    const response = await fetch("http://127.0.0.1:8000/food/add", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        'ngrok-skip-browser-warning': 'true'
      },
      body: JSON.stringify(Foodata)
    })
    if (response.ok){
     GetFood()
     Foodtitle.value = ''
     Foodprice.value = ''
     Foodtaste.value = '' 
  }else{
    const errorData = await response.json();
    alert(`Ошибка: ${errorData.detail || "Не удалось добавить позицию"}`);
  }
  }

  
}

async function AddTicket(){
  if (Ticketcol.value !== "" && Ticketprice.value !== "" && Tickettitle.value !== ""){
     const Ticketdata = {
        title: Tickettitle.value,
        price: Ticketprice.value,
        col: Ticketcol.value,
        user_id: currentAdminId.value
  }
  const response = await fetch("http://127.0.0.1:8000/ticket/add", {
  method: "POST",
  headers: {
    'Content-Type': 'application/json',
    'ngrok-skip-browser-warning': 'true'
  },
  body: JSON.stringify(Ticketdata)
});
   if (response.ok){
    Tickettitle.value = "";
    Ticketprice.value = "";
    Ticketcol.value = ""; 
    await GetTicket()
  }else{
     const errorData = await response.json();
    alert(`Ошибка: ${errorData.detail || "Не удалось добавить билет"}`);
  }
}}

 

const ticket = ref([]);
async function GetTicket() {
  try {
    const serv = await fetch("http://127.0.0.1:8000/Tickets");
    if (serv.ok) {
      const data = await serv.json();
      ticket.value = data;
    }
  } catch (error) {
    console.error("Не удалось загрузить билеты:", error);
  }
}

const food = ref([]);
async function GetFood() {
  try {
    const servfood = await fetch("http://127.0.0.1:8000/food");
    if (servfood.ok) {
      const datafood = await servfood.json();
      food.value = datafood;
    }
  } catch (error) {
    console.error("Не удалось загрузить позиции:", error);
  }
}

const user = ref([]);
async function GetUser() {
  try {
    const bduser = await fetch("http://127.0.0.1:8000/users");
    if (bduser.ok) {
      const datauser = await bduser.json();
      user.value = datauser;
    }
  } catch (error) {
    console.error("Не удалось загрузить пользователей:", error);
  }
}



async function deleteUser(userId) {
  const confirmed = confirm(
    `Вы действительно хотите удалить пользователя #${userId}?`
  );
  if (!confirmed) return;

  try {
    const response = await fetch(`http://127.0.0.1:8000/user/${userId}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        check_user: currentAdminId.value,
      }),
    });

    if (response.ok) {
      alert("Пользователь успешно удален!");
      await GetUser();
    } else {
      const errorData = await response.json();
      alert(`Ошибка: ${errorData.detail || "Не удалось удалить пользователя"}`);
    }
  } catch (error) {
    console.error("Ошибка сети при удалении:", error);
  }
}

async function deleteFood(id) {
  const confirmed = confirm(`Вы действительно хотите удалить позицию #${id}?`);
  if (!confirmed) return;

  try {
    const response = await fetch(`http://127.0.0.1:8000/food/${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        check_user: currentAdminId.value,
      }),
    });

    if (response.ok) {
      alert("Позиция успешно удалена!");
      await GetFood();
    } else {
      const errorData = await response.json();
      alert(`Ошибка: ${errorData.detail || "Не удалось удалить позицию"}`);
    }
  } catch (error) {
    console.error("Ошибка сети при удалении позиции:", error);
  }
}

async function deleteTicket(id) {
  const confirmed = confirm(`Вы действительно хотите удалить билет #${id}?`);
  if (!confirmed) return;

  try {
    const response = await fetch(`http://127.0.0.1:8000/ticket/${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        check_user: currentAdminId.value,
      }),
    });

    if (response.ok) {
      alert("Билет успешно удален!");
      await GetTicket();
    } else {
      const errorData = await response.json();
      alert(`Ошибка: ${errorData.detail || "Не удалось удалить билет"}`);
    }
  } catch (error) {
    console.error("Ошибка сети при удалении билета:", error);
  }
}

async function changeRole(targetUserId, newRole) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/${targetUserId}/role`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        user_id: currentAdminId.value,
        new_role: newRole,
      }),
    });

    if (response.ok) {
      await GetUser();
    } else {
      const errorData = await response.json();
      alert(`Ошибка: ${errorData.detail || "Не удалось изменить роль"}`);
      await GetUser();
    }
  } catch (error) {
    console.error("Ошибка сети при смене роли:", error);
    await GetUser();
  }
}

onMounted(() => {
  GetFood();
  GetTicket();
  GetUser();
});
</script>

<style scoped>
:global(body) {
  margin: 0;
  background-color: #f8fafc;
  font-family: "Inter", system-ui, -apple-system, sans-serif;
}

.admin-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.admin-header {
  background: #ffffff;
  padding: 16px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #e2e8f0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.admin-badge {
  background: #0077b6;
  color: #ffffff;
  font-size: 0.75rem;
  font-weight: 800;
  padding: 4px 8px;
  border-radius: 6px;
  letter-spacing: 1px;
}

.admin-header h1 {
  margin: 0;
  font-size: 1.4rem;
  color: #0f172a;
  font-weight: 800;
}

.back-link {
  color: #0077b6;
  text-decoration: none;
  font-weight: 700;
  font-size: 0.95rem;
  transition: color 0.2s;
}

.back-link:hover {
  color: #00b4d8;
}

.admin-layout {
  display: flex;
  flex: 1;
  max-width: 1400px;
  width: 100%;
  margin: 0 auto;
  padding: 30px 20px;
  gap: 30px;
  box-sizing: border-box;
}

.sidebar {
  width: 240px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.btn-delete {
  padding: 6px 12px;
  background-color: #fef2f2;
  color: #991b1b;
  border: 1px solid #fecaca;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-delete:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  filter: grayscale(1);
}

.btn-delete:hover:not(:disabled) {
  background-color: #fee2e2;
  border-color: #fca5a5;
  color: #7f1d1d;
}

.nav-tab {
  background: transparent;
  border: none;
  text-align: left;
  padding: 14px 18px;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 700;
  color: #64748b;
  cursor: pointer;
  transition: all 0.2s ease;
}

.nav-tab:hover {
  background: #f1f5f9;
  color: #0f172a;
}

.nav-tab.active {
  background: #ffffff;
  color: #0077b6;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  border: 1px solid #e2e8f0;
}

.content-area {
  flex: 1;
}

.panel-header {
  margin-bottom: 24px;
}

.panel-header h2 {
  margin: 0 0 6px 0;
  font-size: 1.8rem;
  color: #0f172a;
  font-weight: 800;
}

.subtitle {
  margin: 0;
  color: #64748b;
  font-size: 0.95rem;
}

.grid-container {
  display: grid;
  grid-template-columns: 360px 1fr;
  gap: 24px;
  align-items: start;
}

.card {
  background: #ffffff;
  border-radius: 18px;
  padding: 24px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
}

.card h3 {
  margin: 0 0 20px 0;
  font-size: 1.2rem;
  color: #0f172a;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 16px;
}

.form-group label {
  font-size: 0.85rem;
  font-weight: 700;
  color: #475569;
}

.custom-input {
  padding: 12px 14px;
  border-radius: 10px;
  border: 1px solid #cbd5e1;
  background-color: #f8fafc;
  font-size: 0.95rem;
  outline: none;
  transition: border-color 0.2s;
}

.custom-input:focus {
  border-color: #0077b6;
  background-color: #ffffff;
}

.primary-btn {
  width: 100%;
  background: #0077b6;
  color: white;
  border: none;
  padding: 12px;
  border-radius: 10px;
  font-weight: 700;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.2s;
  margin-top: 8px;
}

.primary-btn:hover {
  background: #00b4d8;
}

.styled-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

.styled-table th {
  padding: 12px 16px;
  background: #f8fafc;
  color: #475569;
  font-size: 0.85rem;
  font-weight: 700;
  border-bottom: 1px solid #e2e8f0;
}

.styled-table td {
  padding: 14px 16px;
  border-bottom: 1px solid #f1f5f9;
  color: #0f172a;
  font-weight: 600;
  font-size: 0.95rem;
  vertical-align: middle;
}

.role-select {
  box-sizing: border-box;
  padding: 6px 28px 6px 12px;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  outline: none;
  transition: all 0.2s ease;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  background-repeat: no-repeat;
  background-position: right 8px center;
  background-size: 12px;
}

.role-select:disabled {
  cursor: not-allowed;
  opacity: 0.85;
}

.role-select.user {
  background-color: #f8fafc;
  color: #334155;
  border: 1px solid #cbd5e1;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%334155' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

.role-select.employee {
  background-color: #f8fafc;
  color: #0284c7;
  border: 1px solid #bae6fd;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%0284c7' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

.role-select.waiter {
  background-color: #f8fafc;
  color: #7e22ce;
  border: 1px solid #e9d5ff;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%7e22ce' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

.role-select.admin {
  background-color: #f8fafc;
  color: #991b1b;
  border: 1px solid #fecaca;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%991b1b' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
}

.role-select.owner {
  background-color: #f8fafc;
  color: #b45309;
  border: 1px solid #fde68a;
  background-image: none;
  padding-right: 12px;
}

.role-select option.opt-user { background-color: #ffffff; color: #334155; }
.role-select option.opt-employee { background-color: #ffffff; color: #0284c7; }
.role-select option.opt-waiter { background-color: #ffffff; color: #7e22ce; }
.role-select option.opt-admin { background-color: #ffffff; color: #991b1b; }
.role-select option.opt-owner { background-color: #ffffff; color: #b45309; }

@media (max-width: 900px) {
  .admin-layout {
    flex-direction: column;
  }
  .sidebar {
    width: 100%;
    flex-direction: row;
  }
  .grid-container {
    grid-template-columns: 1fr;
  }
}
</style>