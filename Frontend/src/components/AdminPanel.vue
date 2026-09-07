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
          🎫 Билеты
        </button>
        <button 
          class="nav-tab" 
          :class="{ active: activeTab === 'food' }"
          @click="activeTab = 'food'"
        >
          🍔 Еда / Меню
        </button>
        <button 
          class="nav-tab" 
          :class="{ active: activeTab === 'users' }"
          @click="activeTab = 'users'"
        >
          👥 Пользователи
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
                <input type="text" placeholder="Например: Взрослый" class="custom-input" />
              </div>
              <div class="form-group">
                <label>Цена (₽)</label>
                <input type="number" placeholder="3590" class="custom-input" />
              </div>
              <div class="form-group">
                <label>Количество в наличии</label>
                <input type="number" placeholder="100" class="custom-input" />
              </div>
              <button class="primary-btn">Сохранить билет</button>
            </div>
            
            <div class="card table-card">
             <h3>Список билетов</h3>
             <table class="styled-table">
            <thead>
           <tr>
           <th>Название</th>
           <th>Цена</th>
           <th>Id</th>
           <th>Админ</th>
          </tr>
            </thead>
          <tbody>
    <tr v-for="it in ticket" :key="it.id">
      <td>{{ it.title }}</td>
      <td>{{ it.price }}</td>
      <td>{{ it.id }}</td>
      <td>{{ it.admin.name }}</td>
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
                <input type="text" placeholder="Пицца Пепперони" class="custom-input" />
              </div>
              <div class="form-group">
                <label>Описание / Особенности</label>
                <input type="text" placeholder="Острая, с соусом" class="custom-input" />
              </div>
              <div class="form-group">
                <label>Цена (₽)</label>
                <input type="number" placeholder="650" class="custom-input" />
              </div>
              <button class="primary-btn">Добавить в меню</button>
            </div>
             <div class="card table-card">
            <h3>Все позиции</h3>
               <table class="styled-table">
            <thead>
              <tr>
                <th>Название</th>
                <th>Цена</th>
                <th>Вкус</th>
                <th>d</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="it in food" :key="it.id">
                <td>{{ it.name }}</td>
                <td>{{ it.price }}</td>
                <td>{{ it.taste }}</td>
                <td>{{ it.id }}</td>
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
            <table>
              <thead>
                <tr>
                  <th></th>
                </tr>
              </thead>
            </table>

          </div>
        </div>

      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const ticket = ref([])
const activeTab = ref('tickets')

async function GetTicket() { 
  try {
    const serv = await fetch("http://127.0.0.1:8000/Tickets")
    if (serv.ok) {
      const data = await serv.json()
      ticket.value = data
    }
  } catch (error) {
    console.error("Не удалось загрузить билеты:", error)
  }
}

  const food = ref([])

async function GetFood(){
 try{
  const servfood = await fetch("http://127.0.0.1:8000/food")
  if (servfood.ok){
  const datafood = await servfood.json()
  food.value = datafood
  }
 } catch(error){
  console.log("Не удалось загрузить позиции")
 }}



 const user = ref([])
async function GetUser(){
  try{
  bduser = await fetch("http://127.0.0.1:8000/Users")
  if (bduser.ok){
  const datauser = await bduser.json()
  user.value = datauser
  }} catch {
    console.log("Не удалось загрузить пользователей")
  }
}

 onMounted(() => {
  GetFood()
  GetTicket()
  GetUser()
 })
</script>

<style scoped>
:global(body) {
  margin: 0;
  background-color: #f8fafc;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
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
}

.action-btn {
  border: none;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
}

.delete-btn {
  background: #fef2f2;
  color: #dc2626;
}

.delete-btn:hover {
  background: #fee2e2;
}

.edit-btn {
  background: #f0f9ff;
  color: #0284c7;
}

.edit-btn:hover {
  background: #e0f2fe;
}

.role-badge {
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 700;
}

.role-badge.admin {
  background: #f0fdf4;
  color: #16a34a;
}

.role-badge.user {
  background: #f1f5f9;
  color: #475569;
}

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