package app;
import models.*;
import java.lang.reflect.*;

public interface ItemCreator extends InputChecker {
    public static Object createInstanceFromFields(Class<?> clazz) throws Exception {

        Constructor<?>[] constructors = clazz.getDeclaredConstructors();
        
        Constructor<?> constructor = constructors[0];
        
        Field[] fields = clazz.getDeclaredFields();
        
        Object[] parameters = new Object[fields.length];
        
        for (int i = 0; i < fields.length; i++) {
            Field field = fields[i];
            field.setAccessible(true);

            System.out.print("Inserisci il valore per il campo " + field.getName() + " (" + field.getType().getSimpleName() + "): ");
            String input = InputChecker.input_reader.nextLine();
            
            if (field.getType() == String.class) {
                parameters[i] = input;
            } else if (field.getType() == int.class) {
                parameters[i] = Integer.parseInt(input);
            } else if (field.getType() == double.class) {
                parameters[i] = Double.parseDouble(input);
            } else if (field.getType() == boolean.class) {
                parameters[i] = Boolean.parseBoolean(input);
            }
        }
        return constructor.newInstance(parameters);
    }
    
    public static void invokeMethodWithInput(Object obj, String methodName) throws Exception {
        // Ottieni il metodo dalla classe dell'oggetto passato
        Method method = findMethodByName(obj.getClass(), methodName);
        
        // Ottieni i parametri del metodo
        Class<?>[] parameterTypes = method.getParameterTypes();
        
        // Crea un array di oggetti per i parametri
        Object[] parameters = new Object[parameterTypes.length];
        
        // Scanner per l'input dell'utente
        
        // Chiedi all'utente di inserire i valori per ciascun parametro
        for (int i = 0; i < parameterTypes.length; i++) {
            Class<?> paramType = parameterTypes[i];
            System.out.print("Inserisci valore per parametro " + (i + 1) + " (" + paramType.getSimpleName() + "): ");
            String input = InputChecker.input_reader.nextLine();
            
            // Converte l'input in base al tipo del parametro
            if (paramType == String.class) {
                parameters[i] = input;
            } else if (paramType == int.class) {
                parameters[i] = Integer.parseInt(input);
            } else if (paramType == double.class) {
                parameters[i] = Double.parseDouble(input);
            } else if (paramType == boolean.class) {
                parameters[i] = Boolean.parseBoolean(input);
            }
            // Puoi aggiungere altri tipi se necessario
        }
        
        // Invoca il metodo con i parametri ottenuti
        method.setAccessible(true);  // Assicura l'accesso al metodo (anche se è privato)
        method.invoke(obj, parameters);
    }

    private static Method findMethodByName(Class<?> clazz, String methodName) throws NoSuchMethodException {
        // Cerca il metodo nella classe per nome
        for (Method method : clazz.getDeclaredMethods()) {
            if (method.getName().equals(methodName)) {
                return method;
            }
        }
        throw new NoSuchMethodException("Metodo " + methodName + " non trovato nella classe " + clazz.getName());
    }
}
