STARTER_STEP = {
  'name': 'Entrée',
  'items': ('Salade au choix', 'Avocat pesto')
}

MAIN_STEP = {
  'name': "Hors d'oeuvre",
  'items': ('Poissons du jour', 'Pâtes', 'Légumes')
}

DESERT_STEP = {
  'name': "Dessert",
  'items': ('Desserts du jour', 'Café gourmand')
}

MENUS = (
    {
      'name': 'Entrée seule',
      'price': 6.00,
      'steps': (
        STARTER_STEP
      )
    },
    {
      'name': 'Entrée et Plat',
      'price': 11.00,
      'steps': (
        STARTER_STEP,
        MAIN_STEP
      )
    },
    {
      'name': 'Entrée, Plat, Dessert',
      'price': 14.00,
      'steps': (
        STARTER_STEP,
        MAIN_STEP,
        DESERT_STEP
      )
    },
    {
      'name': 'Dessert seul',
      'price': 6.00,
      'steps': (
        DESERT_STEP
      )
    }
)