<<<<<<< HEAD
def get_translation(name):
    # Словарь для перевода
    if name == 'ru':
        return {
            'sex': 'Пол',
            'age': 'Возраст',
            'tongue': 'Налет на языке',
            'stomach': 'Живот',
            'gallbladder_size': 'Желчный пузырь: размер',
            'gallbladder_form': 'Желчный пузырь: форма',
            'gallbladder_wall_thickness': 'Желчный пузырь: толщина стенок',
            'gallbladder_bending': 'Желчный пузырь: изгиб',
            'gallbladder_uniformity_of_walls':
            'Желчный пузырь: однородность стенок',
            'gallbladder_visibility_of_stones':
            'Желчный пузырь: видимость камней',
            'gallbladder_lumen_of_bladder': 'Желчный пузырь: просвет пузыря',
            'pancreas_cysts': 'Поджелудочная: кисты',
            'pancreas_contours': 'Поджелудочная: контуры',
            'pancreas_structure': 'Поджелудочная: структура',
            'pancreas_thickness_of_head': 'Поджелудочная: толщина головки',
            'pancreas_length_of_body': 'Поджелудочная: длина тела',
            'pancreas_echogenicity_of_parenchyma':
            'Поджелудочная: эхогенность паренхимы',
            'pancreas_duct_width': 'Поджелудочная: длина хвоста',
            'FGDS_color': 'ФГДС: цвет',
            'FGDS_deffects': 'ФГДС: деффекты',
            'FGDS_walls_mucus': 'ФГДС: стенки, слизь',
            'FGDS_walls': 'ФГДС: стенки',
            'FGDS_cardia_closes': 'ФГДС: кардия смыкается',
            'nausea': 'Тошнота',
            'pain_upper_abdomen': 'Боли в верхнем отделе живота',
            'upper_quadrant_pain': 'Боли в правом/левом подреберье',
            'vomiting': 'Рвота',
            'abdominal_distention': 'Вздутие живота',
            'pain_on_palpation': 'Боль при пальпации',
            'participation_of_breathing': 'Участие живота в акте дыхания',
            'eructation': 'Отрыжка',
            'heartburn': 'Изжога',
            'weight_loss': 'Снижение массы тела',
            'SOE': 'СОЭ',
            'amylase': 'Амилаза',
            'pancreatic_amylase': 'Панкреатическая амилаза',
            'lipase': 'Липаза',
            'trypsin': 'Трипсин',
            'direct_bilirubin': 'Билирубин прямой',
            'total_bilirubin': 'Билирубин общий',
            'alkaline_phosphatase': 'Щелочная фосфатаза',
            'erythrocytes': 'Эритроциты',
            'hemoglobin': 'Гемоглобин',
            'hematocrit': 'Гематокрит',
            'lymphocytes': 'Лимфациты',
            'neutrophils': 'Нейтрофилы',
            'platelets': 'Тромбоциты',
            'leukocytes': 'Лейкоциты'
        }
    return {}
=======
def get_translation(name):
    # Словарь для перевода
    if name == 'ru':
        return {
            'sex': 'Пол',
            'age': 'Возраст',
            'tongue': 'Налет на языке',
            'stomach': 'Живот',
            'gallbladder_size': 'Желчный пузырь: размер',
            'gallbladder_form': 'Желчный пузырь: форма',
            'gallbladder_wall_thickness': 'Желчный пузырь: толщина стенок',
            'gallbladder_bending': 'Желчный пузырь: изгиб',
            'gallbladder_uniformity_of_walls':
            'Желчный пузырь: однородность стенок',
            'gallbladder_visibility_of_stones':
            'Желчный пузырь: видимость камней',
            'gallbladder_lumen_of_bladder': 'Желчный пузырь: просвет пузыря',
            'pancreas_cysts': 'Поджелудочная: кисты',
            'pancreas_contours': 'Поджелудочная: контуры',
            'pancreas_structure': 'Поджелудочная: структура',
            'pancreas_thickness_of_head': 'Поджелудочная: толщина головки',
            'pancreas_length_of_body': 'Поджелудочная: длина тела',
            'pancreas_echogenicity_of_parenchyma':
            'Поджелудочная: эхогенность паренхимы',
            'pancreas_duct_width': 'Поджелудочная: длина хвоста',
            'FGDS_color': 'ФГДС: цвет',
            'FGDS_deffects': 'ФГДС: деффекты',
            'FGDS_walls_mucus': 'ФГДС: стенки, слизь',
            'FGDS_walls': 'ФГДС: стенки',
            'FGDS_cardia_closes': 'ФГДС: кардия смыкается',
            'nausea': 'Тошнота',
            'pain_upper_abdomen': 'Боли в верхнем отделе живота',
            'upper_quadrant_pain': 'Боли в правом/левом подреберье',
            'vomiting': 'Рвота',
            'abdominal_distention': 'Вздутие живота',
            'pain_on_palpation': 'Боль при пальпации',
            'participation_of_breathing': 'Участие живота в акте дыхания',
            'eructation': 'Отрыжка',
            'heartburn': 'Изжога',
            'weight_loss': 'Снижение массы тела',
            'SOE': 'СОЭ',
            'amylase': 'Амилаза',
            'pancreatic_amylase': 'Панкреатическая амилаза',
            'lipase': 'Липаза',
            'trypsin': 'Трипсин',
            'direct_bilirubin': 'Билирубин прямой',
            'total_bilirubin': 'Билирубин общий',
            'alkaline_phosphatase': 'Щелочная фосфатаза',
            'erythrocytes': 'Эритроциты',
            'hemoglobin': 'Гемоглобин',
            'hematocrit': 'Гематокрит',
            'lymphocytes': 'Лимфациты',
            'neutrophils': 'Нейтрофилы',
            'platelets': 'Тромбоциты',
            'leukocytes': 'Лейкоциты'
        }
    return {}
>>>>>>> 6df53266bb27b333f69d90477c9a2cc2b82fd23d